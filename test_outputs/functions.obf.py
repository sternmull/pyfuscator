def f1(a, b):
    return a - b
print(f1(11, 22))

def _v1(a, b):
    return a - b
print(_v1(b=84, a=853))

def _v5(_arg1, _arg2, _arg3=5):
    return _arg1 - _arg2 * _arg3
print(_v5(10, 90))
print(_v5(7, _arg2=110, _arg3=345))

def _v4(_arg1, _arg4):
    return _arg1 + _arg4
print(_v4('ab', 'cd'))

def outer(a, b, _arg3, _arg5):
    _v7 = '<' + a + '>'

    def _v8(b, x, _arg3):
        return a + b + x + _arg5 + _v7
    return _v8('xx', 'yy', 'CC')
print(outer('aa', 'bb', 'cc', 'dd'))
g1 = 'g1 org val'

def _v6(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'
_v6('hello')
print(g1)
_v2 = '_g2 org val'

def _v3(val):
    global _v2
    _v2 = repr(_v2) + ' # set by _set_g2'
_v3('howdy')
print(_v2)
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