import asyncio
from time import strftime

async def late(delay, msg):
    print(f"Start {msg}")
    await asyncio.sleep(delay)
    print(msg)
    return delay

async def main():
    res = await asyncio.gather(
            late(3, "THREE"),
            late(1, "ONE"),
            late(2, "TWO"),
    )
    print(res)

asyncio.run(main())

