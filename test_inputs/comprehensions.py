def trace(val):
    print(val)
    return val

_x = 'global x' # this is a different x than the one in the comprehensions

[trace((x, y)) for x in 'abc' for y in 'ABC']
print(_x)
{trace((x, y)) for x in 'abc' for y in 'ABC'}
print(_x)
_g = (trace((x, y)) for x in 'qwe' for y in 'rtz')
print(list(_g))
print(_x)
{trace(x) : trace(y) for x in 'uvw' for y in '123'}
print(_x) 

