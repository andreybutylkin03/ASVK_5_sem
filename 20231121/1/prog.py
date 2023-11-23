import sys

buf = sys.stdin.buffer.readline()
i = 1
ll = len(buf)
cur_w = ll - 1
sys.stdout.buffer.write(buf[:1])
N = buf[0]
b = []

while True:
    siz = int(i * cur_w / N)
    b.append(buf[ll - cur_w:ll - cur_w + siz])
    i += 1
    cur_w -= siz
    if cur_w <= 0:
        break

b.sort()
for i in b:
    if i != b'\n':
        sys.stdout.buffer.write(bytearray(i))
