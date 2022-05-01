def f1(a, b):
    return a - b
print(f1(11, 22))

def _v3(a, b):
    _v9 = 'q'
    (_v10, _v8) = 'xy'
    return (a - b, _v10, _v8, _v9)
print(_v3(b=84, a=853))

def _v4(_arg1, _arg2, _arg3=5):
    return _arg1 - _arg2 * _arg3
print(_v4(10, 90))
print(_v4(7, _arg2=110, _arg3=345))

def _v1(_arg1, _arg4):
    return _arg1 + _arg4
print(_v1('ab', 'cd'))

def outer(a, b, _arg3, _arg5):
    _v12 = '<' + a + '>'

    def _v11(b, x, _arg3):
        return a + b + x + _arg5 + _v12
    return _v11('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v7(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v7('hello')
print(g1)
_v2 = '_g2 org val'

def _v6(val):
    global _v2
    _v2 = repr(_v2) + ' # set by _set_g2'
_v6('howdy')
print(_v2)
y = 42

def outer2(j, _arg6):
    _v13 = 23

    def _v14(z):
        nonlocal _v13
        _v13 = z * 2
    _v14(j - _arg6)
    print(_v13)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v15:
        print(_v15, x)
e1('now you know')

def _v5(_v21, /):
    _v18 = list()
    for _v20 in 'abc':
        _v18.append(_v20)
    print(_v20, _v18)
    _v18 = list()
    for (_v17, _v16) in enumerate('ABC'):
        _v18.append((_v17, _v16))
    print(_v17, _v16, _v18)
    _v20 = 2
    for _v19 in range(1, _v21):
        _v20 *= _v19
    print(_v20)
_v5(10)
from contextlib import contextmanager

@contextmanager
def trace_scope(name):
    print('scope entered:', name)
    try:
        yield name
    finally:
        print('scope exited:', name)

def w1():
    with trace_scope('first') as _v23:
        print(_v23)
    with trace_scope('alpha') as _v24, trace_scope('beta') as _v22:
        print(_v24, _v22)
w1()

def importing():
    import re as _v25
    print(_v25.match('.*?(a+)', 'xxxaaa-ay').groups())
importing()

def lambda1(_v27, _v28, /):
    _v26 = lambda _v29, _v30, /: _v27 + _v29 + _v30 + _v28
    return _v26(_v27 * 2, _v28 * 3)
print(lambda1('ab', 'cd'))