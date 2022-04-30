# import re as brr
# import os

# with A(), B() as bb:
#     cc = bb + 3

def bar(x_, y):
    return _foo(3, x)

def _foo(a, b):
    global x
    x = 123

    class Foo:
        def __init__(self):
            self._x = 7
            self._func()
        def _func(self):
            return 3
        def pub(self, k):
            return self._x * 3 + k
    return a + b

# class MyClass:
#     def bar(v, w):
#         pass
_foo(x._func())
x = 123
# x1, x2 = 'ab'

# for ii in f():
#     pass

# x.y = 5

def f(a: 'annotation', _b=1, c=2, *d, e, f=3, **g):
    print(a, b, c, d, e, f, g)

def _my_func(a, b,/):
    print(a, b)

_my_func(12,34)