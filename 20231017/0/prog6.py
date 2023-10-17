from collections import Counter
import timeit

s = input().split()

def f1():
    d = dict()
    for i in s:
        d.setdefault(i, 0)
        d[i] += 1

def f2():
    d = Counter(s)

print(timeit.timeit("f1()", globals = globals(), number = 100))
print(timeit.timeit("f2()", globals = globals(), number = 100))

