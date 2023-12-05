import asyncio
from time import strftime

async def prod(q1):
    for i in range(5):
        await q1.put(f"value_{i}")
        print(f"prod:put value_{i} to q1")
        await asyncio.sleep(1)
    await q1.put(None)

async def mid(q1, q2):
    while True:
        res = await q1.get()
        print(f"mid:got {res} from q1")
        await q2.put(res)
        print(f"mid:put {res} to q2")
        if res == None:
            break

async def cons(q2):
    while True:
        res = await q2.get()
        print(f"cons:got {res} from q2")
        if res == None:
            break

async def main():
    q1, q2 = asyncio.Queue(), asyncio.Queue()
    await asyncio.gather(
        prod(q1),
        mid(q1, q2),
        cons(q2) 
    )

asyncio.run(main())

