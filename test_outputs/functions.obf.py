def f1(a, b):
    return a - b
print(f1(11, 22))

def _a2(a, b):
    _v1 = 'q'
    (_v3, _v2) = 'xy'
    return (a - b, _v3, _v2, _v1)
print(_a2(b=84, a=853))

def _a5(_p1):
    if (_v4 := (_p1 * 2)):
        print('nonzero y')
    else:
        print('y is zero')
    print('y is', _v4)
_a5(5)
_a5(0)

def _a1(_p2, _p3, _p4=5):
    return _p2 - _p3 * _p4
print(_a1(10, 90))
print(_a1(7, _p3=110, _p4=345))

def _a6(_p2, _p1):
    return _p2 + _p1
print(_a6('ab', 'cd'))

def outer(a, b, _p4, _p5):
    _v6 = '<' + a + '>'

    def _v5(b, x, _p4):
        return a + b + x + _p5 + _v6
    return _v5('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _a3(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_a3('hello')
print(g1)
_a7 = '_g2 org val'

def _a4(val):
    global _a7
    _a7 = repr(_a7) + ' # set by _set_g2'
_a4('howdy')
print(_a7)
y = 42

def outer2(j, _p6):
    _v8 = 23

    def _v7(z):
        nonlocal _v8
        _v8 = z * 2
    _v7(j - _p6)
    print(_v8)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v9:
        print(_v9, x)
e1('now you know')

def _a8(_v15, /):
    _v13 = list()
    for _v14 in 'abc':
        _v13.append(_v14)
    print(_v14, _v13)
    _v13 = list()
    for (_v11, _v12) in enumerate('ABC'):
        _v13.append((_v11, _v12))
    print(_v11, _v12, _v13)
    _v14 = 2
    for _v10 in range(1, _v15):
        _v14 *= _v10
    print(_v14)
_a8(10)
from contextlib import contextmanager

@contextmanager
def trace_scope(name):
    print('scope entered:', name)
    try:
        yield name
    finally:
        print('scope exited:', name)

def w1():
    with trace_scope('first') as _v18:
        print(_v18)
    with trace_scope('alpha') as _v16, trace_scope('beta') as _v17:
        print(_v16, _v17)
w1()

def importing():
    import re as _v19
    print(_v19.match('.*?(a+)', 'xxxaaa-ay').groups())
importing()

def lambda1(_v21, _v22, /):
    _v20 = lambda _v23, _v24, /: _v21 + _v23 + _v24 + _v22
    return _v20(_v21 * 2, _v22 * 3)
print(lambda1('ab', 'cd'))