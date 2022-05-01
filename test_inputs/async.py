import asyncio

# ---- async def

async def f1(x, y,/):
    return (x, y)

async def f2():
    print(await f1(11,22))

asyncio.run(f2())

# ---- async for

async def _gen(_n):
    for i in range(_n):
        yield i

async def f3(n,/):
    async for x in _gen(n):
        print('async for', x)

asyncio.run(f3(5))
