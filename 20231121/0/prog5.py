import struct
import random

with open("pr.bin", "wb") as fd:
    for i in range(10):
        fd.write(struct.pack(">f3si", random.random(), bytearray((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),  random.randrange(1, 100000000)))
import os
print(os.path.getsize("pr.bin"))
with open("pr.bin", "rb") as fd:
    for i in range(10):
        f, *b, i = struct.unpack(">f3si", fd.read(11))
        print(f, b, i)

