class _A:
    def __init__(self):
        self._a = 'instance of _A'

    def _afunc(self, x):
        print('_afunc', x)

    def _override(self, x):
        print('_override of _A', x)


class _B(_A):
    def __init__(self):
        super(_B, self).__init__()
        self._a += ' and _B!'
        self._b = 'instance of _B'

    def _bfunc(self, x):
        print('_bfunc', x)

    def _override(self, x):
        print('_override of _B', x)

_b = _B()
print(_b._a)
print(_b._b)
print(_A()._override(11))
print(_B()._override(22))


def f1():
    class Inner: # should always be renamed (just like other local definitions)
        def _f(self):
            print('i am inside a function')
    return Inner()

f1()._f()


class Outer:
    class Inner:
        def _f(self):
            print('i am inside a class')

Outer.Inner()._f()

class _Outer:
    class _InnerBase:
        pass

    class _Inner(_InnerBase):
        pass


class Foo:
    def __private_and_mangled(self, x):
        print('mangled', x)

    def _f(self):
        self.__private_and_mangled(123)

foo = Foo()
foo._f()

try:
    foo.__private_and_mangled
    print('this lookup should have failed!')
    exit(1)
except AttributeError:
    print('this is expcted for lookup of a mangled property from outside the class')



# see https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__
class Philosopher:
    def __init_subclass__(cls, /, _default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = _default_name

class AustralianPhilosopher(Philosopher, _default_name="Bruce"):
    pass

AustralianPhilosopher()
