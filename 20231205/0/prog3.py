import asyncio
from time import strftime

async def snd(evsnd):
    print("snd:generated evsnd")
    evsnd.set()
    print("snd:received evsnd")

async def mid1(evsnd, evmid1):
    print("mid1:generated evmid1")
    await evsnd.wait()
    evmid1.set()
    print("mid1:received evmid1")

async def mid2(evsnd, evmid2):
    print("mid2:generated evmid2")
    await evsnd.wait()
    evmid2.set()
    print("mid2:received evmid2")

async def rcv(evmid1, evmid2):
    print("mid1:generated evmid1, evmid2")
    await evmid1.wait()
    await evmid2.wait()
    print("mid1:received evmid1, evmid2")

async def main():
    evsnd, evmid1, evmid2 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    evsnd.clear()
    evmid1.clear()
    evmid2.clear()
    await asyncio.gather(
            snd(evsnd),
            mid1(evsnd, evmid1),
            mid2(evsnd, evmid2),
            rcv(evmid1, evmid2)
    )

asyncio.run(main())

