import itertools

def slide(seq, n):
    while True:
        a, b = itertools.tee(seq)
        try:
            next(b)
            yield from itertools.islice(a, n)
            seq = b
        except:
            break

import sys
exec(sys.stdin.read())
