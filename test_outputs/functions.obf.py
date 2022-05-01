def f1(a, b):
    return a - b
print(f1(11, 22))

def _v1(a, b):
    _v10 = 'q'
    (_v9, _v8) = 'xy'
    return (a - b, _v9, _v8, _v10)
print(_v1(b=84, a=853))

def _v2(_arg1, _arg2, _arg3=5):
    return _arg1 - _arg2 * _arg3
print(_v2(10, 90))
print(_v2(7, _arg2=110, _arg3=345))

def _v5(_arg1, _arg4):
    return _arg1 + _arg4
print(_v5('ab', 'cd'))

def outer(a, b, _arg3, _arg5):
    _v12 = '<' + a + '>'

    def _v11(b, x, _arg3):
        return a + b + x + _arg5 + _v12
    return _v11('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v3(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v3('hello')
print(g1)
_v6 = '_g2 org val'

def _v7(val):
    global _v6
    _v6 = repr(_v6) + ' # set by _set_g2'
_v7('howdy')
print(_v6)
y = 42

def outer2(j, _arg6):
    _v14 = 23

    def _v13(z):
        nonlocal _v14
        _v14 = z * 2
    _v13(j - _arg6)
    print(_v14)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v15:
        print(_v15, x)
e1('now you know')

def _v4(_v21, /):
    _v18 = list()
    for _v16 in 'abc':
        _v18.append(_v16)
    print(_v16, _v18)
    _v18 = list()
    for (_v17, _v19) in enumerate('ABC'):
        _v18.append((_v17, _v19))
    print(_v17, _v19, _v18)
    _v16 = 2
    for _v20 in range(1, _v21):
        _v16 *= _v20
    print(_v16)
_v4(10)
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