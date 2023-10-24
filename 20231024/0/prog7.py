import itertools

def ffn(n, seq):
    for i in seq:
        yield from itertools.repeat(i, n)


