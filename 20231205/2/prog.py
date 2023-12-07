import asyncio
import random
import copy

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start

    while i < middle or j < finish:
        if j == finish or (i < middle and A[j] > A[i]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

        k += 1

    event_out.set()

async def mtasks(A_old):
    A = copy.deepcopy(A_old)
    B = [0] * len(A)
    tasks = []
    flag = True

    size = 1
    event_buf = [asyncio.Event() for i in range(len(A) + 1)]
    for ev in event_buf:
        ev.set()

    while size < len(A):
        i = 0
        new_event_buf = []
        for start in range(0, len(A), 2 * size):
            middle = min(start + size, len(A) - 1)
            finish = min(start + 2 * size, len(A))

            new_event_buf.append(asyncio.Event())

            if flag:
                tasks.append(asyncio.create_task(merge(A, B, start, middle, finish, event_buf[i], \
                event_buf[i + 1], new_event_buf[-1])))
            else:
                tasks.append(asyncio.create_task(merge(B, A, start, middle, finish, event_buf[i], \
                event_buf[i + 1], new_event_buf[-1])))

            i += 2

            if finish == len(A):
                break

        size *= 2 
        flag = not flag
        new_event_buf.append(new_event_buf[-1])
        event_buf = new_event_buf

    if flag:
        return (tasks, A)
    else:
        return (tasks, B)

import sys
exec(sys.stdin.read())
