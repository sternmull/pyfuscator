
def f1(a, b):
    return a - b

print(f1(11, 22))

def _f2(a, b):
    q = 'q'
    x, y = 'xy'
    return (a - b, x, y, q)

print(_f2(b=84, a=853))

def _walruss(_x):
    if y := _x * 2:
        print('nonzero y', y)
    else:
        print('y is zero')

_walruss(5)
_walruss(0)


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

# ---- exceptions

def e1(x):
    try:
        raise ValueError('bad value')
    except ValueError as e:
        print(e, x)

e1('now you know')

# ---- for loops

def _for1(n,/):
    acc = list()
    for x in 'abc':
        acc.append(x)
    print(x, acc)

    acc = list()
    for a, b in enumerate('ABC'):
        acc.append((a, b))
    print(a, b, acc)

    x = 2
    for i in range(1, n):
        x *= i
    print(x)

_for1(10)

# ---- with

from contextlib import contextmanager

@contextmanager
def trace_scope(name):
    print('scope entered:', name)
    try:
        yield name
    finally:
        print('scope exited:', name)

def w1():
    with trace_scope('first') as s:
        print(s)

    with trace_scope('alpha') as a, trace_scope('beta') as b:
        print(a, b)

w1()

# ---- local imports

def importing():
    import re as my_re
    print(my_re.match(r'.*?(a+)', 'xxxaaa-ay').groups())

importing()

# ---- lambda

def lambda1(a, b,/):
    f = lambda x, y,/: a + x + y + b
    return f(a*2, b*3)

print(lambda1('ab', 'cd'))
