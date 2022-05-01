class _v1:

    def __init__(self):
        self._a3 = 'instance of _A'

    def _a1(self, x):
        print('_afunc', x)

    def _a2(self, x):
        print('_override of _A', x)

class _v2(_v1):

    def __init__(self):
        super(_v2, self).__init__()
        self._a3 += ' and _B!'
        self._a5 = 'instance of _B'

    def _a4(self, x):
        print('_bfunc', x)

    def _a2(self, x):
        print('_override of _B', x)
_v3 = _v2()
print(_v3._a3)
print(_v3._a5)
print(_v1()._a2(11))
print(_v2()._a2(22))

def f1():

    class _v5:

        def _a6(self):
            print('i am inside a function')
    return _v5()
f1()._a6()

class Outer:

    class Inner:

        def _a6(self):
            print('i am inside a class')
Outer.Inner()._a6()

class _v4:

    class _a8:
        pass

    class _a7(_a8):
        pass