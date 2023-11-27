import sys

buf = sys.stdin.buffer.readline()
if buf[-1] == 10:
    buf = buf[:-1]
i = 0
L = len(buf) - 1
sys.stdout.buffer.write(buf[:1])
N = buf[0]
b = []

while True:
    b.append(buf[1 + i * L // N:1 + (i + 1) * L // N])
    i += 1
    if i * L / N >= L:
        break

b.sort()
for i in b:
    if i != b'\n':
        sys.stdout.buffer.write(bytearray(i))
