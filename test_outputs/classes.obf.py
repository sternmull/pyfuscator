class _a4:

    def __init__(self):
        self._a7 = 'instance of _A'

    def _a5(self, x):
        print('_afunc', x)

    def _a6(self, x):
        print('_override of _A', x)

class _a3(_a4):

    def __init__(self):
        super(_a3, self).__init__()
        self._a7 += ' and _B!'
        self._a1 = 'instance of _B'

    def _a8(self, x):
        print('_bfunc', x)

    def _a6(self, x):
        print('_override of _B', x)
_a1 = _a3()
print(_a1._a7)
print(_a1._a1)
print(_a4()._a6(11))
print(_a3()._a6(22))

def f1():

    class _v1:

        def _a9(self):
            print('i am inside a function')
    return _v1()
f1()._a9()

class Outer:

    class Inner:

        def _a9(self):
            print('i am inside a class')
Outer.Inner()._a9()

class _a2:

    class _a11:
        pass

    class _a10(_a11):
        pass