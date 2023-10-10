from math import sin

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A
X = 60
Y = 20

A, B = -5, 5

ans = [[' '] * X for i in range(Y)]

for i in range(X):
    x = scale(0, X - 1, A, B, i)
    y = sin(x)
    w = scale(-1, 1, Y - 1, 0, y)
    ans[int(w)][i] = '*'

print('\n'.join(["".join(i) for i in ans]))

