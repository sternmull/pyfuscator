def foo(_v3, _v4, /, c):
    return _v3 + _v4 + c
print(foo(11, 22, 33))

def _v2(_v5, _v6, /):
    return _v5 + _v6
print(_v2(111, 222))

def pub_global_user():
    global y
    y = 123
pub_global_user()
print(y)
y = 'y str'
print(y)

def priv_global_user():
    global _v1
    _v1 = 123
priv_global_user()
print(_v1)
_v1 = '_y str'
print(_v1)