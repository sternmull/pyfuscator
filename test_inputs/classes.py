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

