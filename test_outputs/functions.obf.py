def f1(a, b):
    return a - b
print(f1(11, 22))

def _v6(a, b):
    _v11 = 'q'
    (_v9, _v10) = 'xy'
    return (a - b, _v9, _v10, _v11)
print(_v6(b=84, a=853))

def _v7(_arg1):
    if (_v12 := (_arg1 * 2)):
        print('nonzero y', _v12)
    else:
        print('y is zero')
_v7(5)
_v7(0)

def _v5(_arg2, _arg3, _arg4=5):
    return _arg2 - _arg3 * _arg4
print(_v5(10, 90))
print(_v5(7, _arg3=110, _arg4=345))

def _v3(_arg2, _arg1):
    return _arg2 + _arg1
print(_v3('ab', 'cd'))

def outer(a, b, _arg4, _arg5):
    _v14 = '<' + a + '>'

    def _v13(b, x, _arg4):
        return a + b + x + _arg5 + _v14
    return _v13('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v1(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v1('hello')
print(g1)
_v4 = '_g2 org val'

def _v8(val):
    global _v4
    _v4 = repr(_v4) + ' # set by _set_g2'
_v8('howdy')
print(_v4)
y = 42

def outer2(j, _arg6):
    _v15 = 23

    def _v16(z):
        nonlocal _v15
        _v15 = z * 2
    _v16(j - _arg6)
    print(_v15)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v17:
        print(_v17, x)
e1('now you know')

def _v2(_v23, /):
    _v19 = list()
    for _v21 in 'abc':
        _v19.append(_v21)
    print(_v21, _v19)
    _v19 = list()
    for (_v18, _v20) in enumerate('ABC'):
        _v19.append((_v18, _v20))
    print(_v18, _v20, _v19)
    _v21 = 2
    for _v22 in range(1, _v23):
        _v21 *= _v22
    print(_v21)
_v2(10)
from contextlib import contextmanager

@contextmanager
def trace_scope(name):
    print('scope entered:', name)
    try:
        yield name
    finally:
        print('scope exited:', name)

def w1():
    with trace_scope('first') as _v26:
        print(_v26)
    with trace_scope('alpha') as _v25, trace_scope('beta') as _v24:
        print(_v25, _v24)
w1()

def importing():
    import re as _v27
    print(_v27.match('.*?(a+)', 'xxxaaa-ay').groups())
importing()

def lambda1(_v29, _v30, /):
    _v28 = lambda _v31, _v32, /: _v29 + _v31 + _v32 + _v30
    return _v28(_v29 * 2, _v30 * 3)
print(lambda1('ab', 'cd'))