def trace(val):
    print(val)
    return val
_a2 = 'global x'
[trace((_v1, _v2)) for _v1 in 'abc' for _v2 in 'ABC']
print(_a2)
{trace((_v3, _v4)) for _v3 in 'abc' for _v4 in 'ABC'}
print(_a2)
_a1 = (trace((_v5, _v6)) for _v5 in 'qwe' for _v6 in 'rtz')
print(list(_a1))
print(_a2)
{trace(_v7): trace(_v8) for _v7 in 'uvw' for _v8 in '123'}
print(_a2)