def f1(a, b):
    return a - b
print(f1(11, 22))

def _v2(a, b):
    _v10 = 'q'
    (_v9, _v11) = 'xy'
    return (a - b, _v9, _v11, _v10)
print(_v2(b=84, a=853))

def _v1(_arg1):
    if (_v12 := (_arg1 * 2)):
        print('nonzero y', _v12)
    else:
        print('y is zero')
_v1(5)
_v1(0)

def _v3(_arg2, _arg3, _arg4=5):
    return _arg2 - _arg3 * _arg4
print(_v3(10, 90))
print(_v3(7, _arg3=110, _arg4=345))

def _v4(_arg2, _arg1):
    return _arg2 + _arg1
print(_v4('ab', 'cd'))

def outer(a, b, _arg4, _arg5):
    _v14 = '<' + a + '>'

    def _v13(b, x, _arg4):
        return a + b + x + _arg5 + _v14
    return _v13('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v7(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v7('hello')
print(g1)
_v5 = '_g2 org val'

def _v8(val):
    global _v5
    _v5 = repr(_v5) + ' # set by _set_g2'
_v8('howdy')
print(_v5)
y = 42

def outer2(j, _arg6):
    _v16 = 23

    def _v15(z):
        nonlocal _v16
        _v16 = z * 2
    _v15(j - _arg6)
    print(_v16)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v17:
        print(_v17, x)
e1('now you know')

def _v6(_v23, /):
    _v20 = list()
    for _v18 in 'abc':
        _v20.append(_v18)
    print(_v18, _v20)
    _v20 = list()
    for (_v21, _v22) in enumerate('ABC'):
        _v20.append((_v21, _v22))
    print(_v21, _v22, _v20)
    _v18 = 2
    for _v19 in range(1, _v23):
        _v18 *= _v19
    print(_v18)
_v6(10)
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
    with trace_scope('alpha') as _v24, trace_scope('beta') as _v25:
        print(_v24, _v25)
w1()

def importing():
    import re as _v27
    print(_v27.match('.*?(a+)', 'xxxaaa-ay').groups())
importing()

def lambda1(_v29, _v30, /):
    _v28 = lambda _v31, _v32, /: _v29 + _v31 + _v32 + _v30
    return _v28(_v29 * 2, _v30 * 3)
print(lambda1('ab', 'cd'))