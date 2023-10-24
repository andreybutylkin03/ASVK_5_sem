import itertools

def ffn(n, seq):
    yield from itertools.filterfalse(lambda x: x%n, seq)

