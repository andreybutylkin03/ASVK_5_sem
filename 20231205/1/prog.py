import asyncio

async def writer(q, delay, event):
    await asyncio.sleep(delay)
    i = 0

    while True:
        await q.put(f"{i}_{delay}")
        i += 1
        if event.is_set():
            break
        await asyncio.sleep(delay)

async def stacker(q, st, event):
    while True:
        await asyncio.sleep(0)
        res = await q.get()
        await st.put(res)
        if event.is_set():
            break

async def reader(st, num, delay, event):
    await asyncio.sleep(delay)
    i = 0

    while i < num:
        res = await st.get()
        if res is not None:
            print(res)
            i += 1
        await asyncio.sleep(delay)

    event.set()

async def main(del1, del2, del3, num):
    q = asyncio.Queue()
    event = asyncio.Event()
    event.clear()
    st = asyncio.LifoQueue()

    await asyncio.gather(
        writer(q, del1, event),
        writer(q, del2, event),
        stacker(q, st, event),
        reader(st, num, del3, event)
    )

del1, del2, del3, num = eval(input())
asyncio.run(main(del1, del2, del3, num))
