def foo(a, b,/, c):
    return a + b + c

print(foo(11, 22, 33))

def _foo(a, b,/):
    return a + b

print(_foo(111, 222))

def pub_global_user():
    global y
    y = 123

pub_global_user()
print(y)
y = 'y str'
print(y)

def priv_global_user():
    global _y
    _y = 123

priv_global_user()
print(_y)
_y = '_y str'
print(_y)
