_a1 = 'hello'
b = 'world'
print(_a1, b)

def foo(_v1, _v2, /, c):
    return _v1 + _v2 + c
print(foo(11, 22, 33))

def _a4(_v3, _v4, /):
    return _v3 + _v4
print(_a4(111, 222))

def pub_global_user():
    global y
    y = 123
pub_global_user()
print(y)
y = 'y str'
print(y)

def priv_global_user():
    global _a2
    _a2 = 123
priv_global_user()
print(_a2)
_a2 = '_y str'
print(_a2)
import re as my_re
_a3 = my_re.match('a+(b+).*', 'aaabbccc')
print(_a3.groups())