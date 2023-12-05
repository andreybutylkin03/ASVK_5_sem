import asyncio
from time import strftime

async def squarer(a):
    return a*a

async def doubler(a):
    return 2 * a

async def main(a, b):
    mas = [a, b]

    res = await asyncio.gather(squarer(mas[0]), squarer(mas[1]))
    res = await asyncio.gather(doubler(mas[0]), doubler(mas[1]))
    print(res)

