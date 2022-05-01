import asyncio

async def f1(_v1, _v2, /):
    return (_v1, _v2)

async def f2():
    print(await f1(11, 22))
asyncio.run(f2())

async def _a1(_p1):
    for _v3 in range(_p1):
        yield _v3

async def f3(_v6, /):
    async for _v5 in _a1(_v6):
        print('async for', _v5)
    print(_v5)
    _v4 = [_v7 + 100 async for _v7 in _a1(3)]
    print(_v5)
    print(_v4)
asyncio.run(f3(5))