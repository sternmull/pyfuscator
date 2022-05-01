def trace(val):
    print(val)
    return val
_v1 = 'global x'
[trace((_v3, _v4)) for _v3 in 'abc' for _v4 in 'ABC']
print(_v1)
{trace((_v5, _v6)) for _v5 in 'abc' for _v6 in 'ABC'}
print(_v1)
_v2 = (trace((_v7, _v8)) for _v7 in 'qwe' for _v8 in 'rtz')
print(list(_v2))
print(_v1)
{trace(_v9): trace(_v10) for _v9 in 'uvw' for _v10 in '123'}
print(_v1)