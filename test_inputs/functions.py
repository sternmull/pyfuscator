
def f1(a, b):
    return a - b

print(f1(11, 22))

def _f2(a, b):
    return a - b

print(_f2(b=84, a=853))

def _f3(_a, _b, _c=5): # arguments will be renamed because of underscore
    return _a - _b * _c

print(_f3(10, 90))
print(_f3(7, _b=110, _c=345))

def _f4(_a, _x): # arguments will be renamed because of underscore
    return _a + _x

print(_f4('ab', 'cd'))


def outer(a, b, _c, _d):
    v = '<' + a + '>'
    def inner(b, x, _c):
        return a + b + x + _d + v

    return inner('xx', 'yy', 'CC')

print(outer('aa', 'bb', 'cc', 'dd'))


# ---- global
g1 = 'g1 org val'

def _set_g1(val):
    global g1
    g1 = repr(g1) + ' # set by _set_g1'

_set_g1('hello')
print(g1)

_g2 = '_g2 org val'

def _set_g2(val):
    global _g2
    _g2 = repr(_g2) + ' # set by _set_g2'

_set_g2('howdy')
print(_g2)


# ----- nonlocal

y = 42

def outer2(j, _k):
    y = 23
    def inner(z):
        nonlocal y
        y = z * 2

    inner(j - _k)
    print(y)

outer2(543, 2323)
print(y)
