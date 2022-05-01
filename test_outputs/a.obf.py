_v1 = 'hello'
b = 'world'
print(_v1, b)

def foo(_v6, _v7, /, c):
    return _v6 + _v7 + c
print(foo(11, 22, 33))

def _v3(_v8, _v9, /):
    return _v8 + _v9
print(_v3(111, 222))

def pub_global_user():
    global y
    y = 123
pub_global_user()
print(y)
y = 'y str'
print(y)

def priv_global_user():
    global _v4
    _v4 = 123
priv_global_user()
print(_v4)
_v4 = '_y str'
print(_v4)
import re as _v5
_v2 = _v5.match('a+(b+).*', 'aaabbccc')
print(_v2.groups())