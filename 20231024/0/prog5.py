import itertools

def foo():
    res = 0
    for i in itertools.count(1):
        res += i ** (-2)
        yield res
ite = itertools.dropwhile(lambda x: x < 1.6, foo())
print(*[next(ite) for i in range(10)], sep='\n')
