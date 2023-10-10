from math import sin

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

N = 30
A, B = -5, 5
for i in range(N):
    x = scale(0, N - 1, -5, 5, i)
    y = sin(x)
    w = scale(-1, 1, 0, 20, y)
    print(int(w) * " ", "*")


