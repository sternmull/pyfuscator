import asyncio

async def f1(_v2, _v3, /):
    return (_v2, _v3)

async def f2():
    print(await f1(11, 22))
asyncio.run(f2())

async def _v1(_p1):
    for _v4 in range(_p1):
        yield _v4

async def f3(_v7, /):
    async for _v6 in _v1(_v7):
        print('async for', _v6)
    print(_v6)
    _v5 = [_v8 + 100 async for _v8 in _v1(3)]
    print(_v6)
    print(_v5)
asyncio.run(f3(5))