"""
TODO:
- tests
- renamer
  - class arguments
  - f-strings
  - match
  - comprehensions
"""


import ast

def _names(nameOrTuple):
    if isinstance(nameOrTuple, ast.Name):
        return [nameOrTuple.id]
    elif isinstance(nameOrTuple, ast.Tuple):
        return [name.id for name in nameOrTuple.elts]
    else:
        assert(isinstance(nameOrTuple, ast.Attribute))
        return []

class BodyDefCollector(ast.NodeVisitor):
    def __init__(self, root):
        self._root = root
        self.locals = set() # also x for "import foo as x"
        self.globals = set()
        self.nonlocals = set()
        self.imports = set() # x for "import x"

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

    def visit_FunctionDef(self, node):
        return self._visit_def(node)

    def visit_AsyncFunctionDef(self, node):
        return self._visit_def(node)

    def visit_Assign(self, node):
        for t in node.targets:
            for name in _names(t):
                self._add_local(name)

    def visit_Import(self, node):
        for alias in node.names:
            if alias.asname:
                self._add_local(alias.asname)
            else:
                self.imports.add(alias.name)

    def visit_ClassDef(self, node):
        self._visit_def(node)

    def visit_Global(self, node):
        for name in node.names:
            self._add_global(name)

    def visit_Nonlocal(self, node):
        for name in node.names:
            self._add_nonlocal(name)

    def visit_For(self, node):
        for name in _names(node.target):
            self._add_local(name)

        self.generic_visit(node)

    def visit_With(self, node):
        for item in node.items:
            if item.optional_vars:
                self._add_local(item.optional_vars.id)

        self.generic_visit(node)

    # TODO: visist_Match for as_pattern and capture_pattern and maybe more!


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
        self._inClass = False
        self._attr2new = dict()

    def _is_nonpublic(self, name):
        if name.startswith('__'):
            return False # don't rename special attributes

        if not name.startswith('_'):
            return False # don't rename non-private attributes

        return True

    def _new_name(self, orgName):
        self._lastNameId += 1
        return f'_v{self._lastNameId}'

    def _attr_name(self, orgName):
        try:
            return self._attr2new[orgName]
        except KeyError:
            if self._is_nonpublic(orgName):
                self._lastAttrId += 1
                new = f'_a{self._lastAttrId}'
            else:
                new = orgName

            self._attr2new[orgName] = new
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

        scope = {name : self._new_name(name) for name in get_body_defs(node).locals if self._is_nonpublic(name)}
        self._enter(scope)

        return self.generic_visit(node)

    def visit_Name(self, node):
        node.id = self._resolve(node.id)
        return node

    def visit_FunctionDef(self, node):
        if self._inClass:
            node.name = self._attr_name(node.name)
        else:
            node.name = self._resolve(node.name)

        wasInClass = self._inClass
        self._inClass = False

        defs = get_body_defs(node)
        scope = {name : self._new_name(name) for name in defs.locals - defs.globals - defs.nonlocals}

        args : ast.arguments = node.args
        for arg in args.args:
            org = arg.arg
            if self._is_nonpublic(org):
                arg.arg = scope[org] = self._new_name(org)

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
        self._inClass = wasInClass
        return ret

    def visit_AsyncFunctionDef(self, node):
        return self.visit_FunctionDef(node)

    def _visit_xxxal(self, node):
        node.names = map(self._resolve, node.names)
        return node

    def visit_Global(self, node):
        return self._visit_xxxal(node)

    def visit_Nonlocal(self, node):
        return self._visit_xxxal(node)

    def visit_ClassDef(self, node):
        if self._inClass:
            node.name = self._attr_name(node.name)
        else:
            node.name = self._resolve(node.name)

        wasInClass = self._inClass
        self._inClass = True

        ret = self.generic_visit(node)
        self._inClass = wasInClass
        return ret

    def visit_Attribute(self, node):
        node.attr = self._attr_name(node.attr)
        return self.generic_visit(node)


def main():
    with open('input.py') as f:
        s = f.read()

    root = ast.parse(s)

    for name in get_body_defs(root).locals:
        print(name)

    root = Renamer().visit(root)


    with open('output.py', 'w') as f:
        f.write(ast.unparse(root))


if __name__ == '__main__':
    main()
