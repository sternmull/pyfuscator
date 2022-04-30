def f1(a, b):
    return a - b
print(f1(11, 22))

def _v6(a, b):
    return a - b
print(_v6(b=84, a=853))

def _v2(_arg1, _arg2, _arg3=5):
    return _arg1 - _arg2 * _arg3
print(_v2(10, 90))
print(_v2(7, _arg2=110, _arg3=345))

def _v3(_arg1, _arg4):
    return _arg1 + _arg4
print(_v3('ab', 'cd'))

def outer(a, b, _arg3, _arg5):
    _v8 = '<' + a + '>'

    def _v7(b, x, _arg3):
        return a + b + x + _arg5 + _v8
    return _v7('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v4(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v4('hello')
print(g1)
_v5 = '_g2 org val'

def _v1(val):
    global _v5
    _v5 = repr(_v5) + ' # set by _set_g2'
_v1('howdy')
print(_v5)
y = 42

def outer2(j, _arg6):
    _v10 = 23

    def _v9(z):
        nonlocal _v10
        _v10 = z * 2
    _v9(j - _arg6)
    print(_v10)
outer2(543, 2323)
print(y)

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as _v11:
        print(_v11, x)
e1('now you know')
from contextlib import contextmanager

@contextmanager
def trace_scope(name):
    print('scope entered:', name)
    try:
        yield name
    finally:
        print('scope exited:', name)

def w1():
    with trace_scope('first') as _v14:
        print(_v14)
    with trace_scope('alpha') as _v12, trace_scope('beta') as _v13:
        print(_v12, _v13)
w1()