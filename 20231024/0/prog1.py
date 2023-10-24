import itertools

def foo():
    summ = 0
    for i in itertools.count(1):
        summ += i**(-2)
        yield summ

