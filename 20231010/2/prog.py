from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

*a, f = input().split()
W, H, A, B = map(float, a)

def F(x):
    return eval(f)

y = []

for i in range(int(W)):
    y.append(F(scale(0, W - 1, A, B, i)))

mi = min(y)
ma = max(y)

ans = [[' '] * int(W) for i in range(int(H))]

i = 0
wp = 0

while i < W:
    w = scale(mi, ma, H - 1, 0, y[i])
    ans[round(w)][int(i)] = '*'
    if i:
        vr = abs(round(w) - round(wp)) - 1
        if w > wp:
            for j in range(round(vr / 2)):
                ans[round(wp) + j + 1][i - 1] = '*'
            for j in range(round(vr / 2), int(vr)):
                ans[round(wp) + j + 1][i] = '*'
        elif w < wp:
            for j in range(round(vr / 2)):
                ans[round(wp) - (j + 1)][i - 1] = '*'
            for j in range(round(vr / 2), int(vr)):
                ans[round(wp) - (j + 1)][i] = '*'

    i += 1
    wp = round(w)

print('\n'.join([''.join(i) for i in ans]))
