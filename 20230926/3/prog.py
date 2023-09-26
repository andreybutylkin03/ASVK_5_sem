n = 0
a = []

while (vr := input()) and vr:
    a.append(eval(vr))
    n += 1

n //= 2

b = a[n:]
a = a[:n] 
c = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        c[i][j] = 0
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]

for i in range(n):
    print(*c[i], sep=',')
