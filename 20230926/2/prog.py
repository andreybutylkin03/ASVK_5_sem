def booble(a, f):
    le = len(a)
    for i in range(le):
        for j in range(le - 1, i, -1):
            if f(a[j - 1]) > f(a[j]):
                a[j - 1], a[j] = a[j], a[j - 1]

a = list(eval(input()))
booble(a, lambda x: x ** 2 % 100)
print(a)
