import string
import timeit

s = input()
ss = set(string.ascii_lowercase)
gg = set("euyioa")
ss -= gg

def f():
    return (len(set(s) & gg), len(set(s) & ss))

print(timeit.timeit("f()", globals = globals(), number=100))


