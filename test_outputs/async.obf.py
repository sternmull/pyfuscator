import asyncio

async def f1(_v2, _v3, /):
    return (_v2, _v3)

async def f2():
    print(await f1(11, 22))
asyncio.run(f2())

async def _v1(_arg1):
    for _v4 in range(_arg1):
        yield _v4

async def f3(_v6, /):
    async for _v5 in _v1(_v6):
        print('async for', _v5)
asyncio.run(f3(5))