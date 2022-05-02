"""
TODO:
- preserve hashbang comments
- reproduce exceution bit for output files
- renamer
  - use __all__ on module level
  - support configurable blacklists for names (seperate vars, params, attribs?) that should not be replaced
  - Make sure to not use identifiers that are already present.
    Actually i am not sure collisions are practically possible right now, maybe it is already safe!
  - reuse names from outer scopes as much as possible to make it harder to tell apart different variables (many name collisions until you take scope into account)
  - Commandline options to obfuscate multiple files?
    In general support and test multi-file operation that allows to access private attributes of other modules.
- remove code that is not used (private functions/classes that are not used anywhere)
"""


import ast
import re

def _names(nameOrNames):
    if isinstance(nameOrNames, ast.Name):
        return [nameOrNames.id]
    elif isinstance(nameOrNames, (ast.Tuple, ast.List)):
        return [name.id for name in nameOrNames.elts]
    else:
        assert(isinstance(nameOrNames, ast.Attribute))
        return []

class BodyDefCollector(ast.NodeVisitor):
    def __init__(self, root):
        self._root = root
        self.locals = set()
        self.globals = set()
        self.nonlocals = set()
        self.imports = set() # x for "import x"
        self.imports_as = set() # y for "import x as y"

    def _add_local(self, name):
        self.locals.add(name)

    def _add_nonlocal(self, name):
        self.nonlocals.add(name)

    def _add_global(self, name):
        self.globals.add(name)

    def _visit_def(self, node):
        if node is self._root:
            self.generic_visit(node)
        else:
            self._add_local(node.name)

    visit_FunctionDef = _visit_def
    visit_AsyncFunctionDef = _visit_def
    visit_ClassDef = _visit_def

    def visit_Assign(self, node):
        for t in node.targets:
            for name in _names(t):
                self._add_local(name)

    def visit_NamedExpr(self, node):
        self._add_local(node.target.id)

    def visit_MatchAs(self, node):
        self._add_local(node.name)

    def visit_Import(self, node):
        for alias in node.names:
            if alias.asname:
                self.imports_as.add(alias.asname)
            else:
                self.imports.add(alias.name)

    def visit_Global(self, node):
        for name in node.names:
            self._add_global(name)

    def visit_Nonlocal(self, node):
        for name in node.names:
            self._add_nonlocal(name)

    def _visit_for(self, node):
        for name in _names(node.target):
            self._add_local(name)

        self.generic_visit(node)

    visit_For = _visit_for
    visit_AsyncFor = _visit_for

    def visit_With(self, node):
        for item in node.items:
            for name in _names(item.optional_vars):
                self._add_local(item.optional_vars.id)

        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.name:
            self._add_local(node.name)

        self.generic_visit(node)

    # TODO: visit_Match for as_pattern and capture_pattern and maybe more!


def get_body_defs(node):
    """
    Returns the definitions that are local to (the body of) a node.
    Names that are defined in node itself (as it is the case for
    arguments for function definitions) are not included.
    """
    x = BodyDefCollector(node)
    x.visit(node)
    return x

class Renamer(ast.NodeTransformer):
    def __init__(self):
        self._lastNameId = 0
        self._org2new = list() # topmost scope is the first
        self._lastAttrId = 0
        self._attr2new = dict()
        self._lastArgId = 0
        self._arg2new = dict()

    def _is_private(self, name):
        # see https://docs.python.org/3/tutorial/classes.html#private-variables
        return name.startswith('_') and not name.endswith('__')

    def _new_name(self, orgName):
        self._lastNameId += 1
        return f'_v{self._lastNameId}'

    def _attr_name(self, orgName, inClass=False):
        try:
            return self._attr2new[orgName]
        except KeyError:
            if self._is_private(orgName):
                self._lastAttrId += 1
                new = f'_a{self._lastAttrId}'
                if inClass and orgName.startswith('__'):
                    new = '_' + new
            else:
                new = orgName

            self._attr2new[orgName] = new
            return new

    def _arg_name(self, orgName): # TODO: deduplicate with _attr_name
        try:
            return self._arg2new[orgName]
        except KeyError:
            if self._is_private(orgName):
                self._lastArgId += 1
                new = f'_p{self._lastArgId}'
            else:
                new = orgName

            self._arg2new[orgName] = new
            return new

    def _enter(self, scope):
        self._org2new.insert(0, scope)

    def _exit(self):
        self._org2new.pop(0)

    def _resolve(self, name):
        for scope in self._org2new:
            try:
                return scope[name]
            except KeyError:
                pass

        return name

    def visit_Module(self, node):
        assert(len(self._org2new) == 0)

        defs = get_body_defs(node)
        scope = {name : self._attr_name(name) for name in defs.locals if self._is_private(name)} | \
                {name : self._attr_name(name) for name in defs.imports_as}
        self._enter(scope)
        ret = self.generic_visit(node)
        self._exit()
        return ret

    def visit_Name(self, node):
        node.id = self._resolve(node.id)
        return node

    def visit_Import(self, node):
        node.names = list(node.names)
        for alias in node.names:
            if alias.asname:
                alias.asname = self._resolve(alias.asname)
        return self.generic_visit(node)

    def _visit_function_or_lambda(self, node):
        defs = get_body_defs(node)
        scope = {name : self._new_name(name) for name in defs.locals - defs.globals - defs.nonlocals} | \
                {name : self._new_name(name) for name in defs.imports_as}

        args : ast.arguments = node.args
        for arg in args.args:
            org = arg.arg
            arg.arg = scope[org] = self._arg_name(org)

        for arg in args.posonlyargs:
            org = arg.arg
            arg.arg = scope[org] = self._new_name(org)

        if args.vararg:
            org = args.vararg.arg
            new = args.vararg.arg = self._new_name(org)
            scope[org] = new

        if args.kwarg:
            org = args.kwarg.arg
            new = args.kwarg.arg = self._new_name(org)
            scope[org] = new

        self._enter(scope)
        ret = self.generic_visit(node)
        self._exit()
        return ret

    def visit_FunctionDef(self, node):
        node.name = self._resolve(node.name)
        return self._visit_function_or_lambda(node)

    visit_AsyncFunctionDef = visit_FunctionDef
    visit_Lambda = _visit_function_or_lambda

    def visit_Call(self, node):
        for kw in node.keywords:
            if kw.arg:
                kw.arg = self._arg_name(kw.arg)

        return self.generic_visit(node)

    def _visit_xxxal(self, node):
        node.names = [self._resolve(name) for name in node.names]
        return node

    visit_Global = _visit_xxxal
    visit_Nonlocal = _visit_xxxal

    def visit_ClassDef(self, node : ast.ClassDef):
        node.name = self._resolve(node.name)

        defs = get_body_defs(node)
        scope = {name : self._attr_name(name, True) for name in defs.locals - defs.globals - defs.nonlocals} | \
                {name : self._attr_name(name, True) for name in defs.imports_as}

        for kw in node.keywords:
            org = kw.arg
            kw.arg = scope[org] = self._arg_name(org)

        self._enter(scope)
        ret = self.generic_visit(node)
        self._exit()
        return ret

    def visit_Attribute(self, node):
        node.attr = self._attr_name(node.attr)
        return self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.name:
            node.name = self._resolve(node.name)

        return self.generic_visit(node)

    def _visit_XxxComp(self, node):
        scope = {g.target.id : self._new_name(g.target.id) for g in node.generators}
        self._enter(scope)
        for g in node.generators:
            g.target.id = self._resolve(g.target.id)
        ret = self.generic_visit(node)
        self._exit()
        return ret

    visit_ListComp = _visit_XxxComp
    visit_SetComp = _visit_XxxComp
    visit_DictComp = _visit_XxxComp
    visit_GeneratorExp = _visit_XxxComp

    def visit_MatchAs(self, node):
        node.name = self._resolve(node.name)
        return node

def _main():
    import argparse
    parser = argparse.ArgumentParser(description='Obfuscate a Python script')
    parser.add_argument('input', type=str,
                        help='path to the input script')

    parser.add_argument('-o', '--output', type=str,
                        help='path to the output script')

    args = parser.parse_args()
    obfuscate(args.input, args.output)

def obfuscate(in_fn, out_fn):
    with open(in_fn) as f:
        s = f.read()

    root = ast.parse(s)

    root = Renamer().visit(root)

    with open(out_fn, 'w') as f:
        f.write(ast.unparse(root))


if __name__ == '__main__':
    _main()
