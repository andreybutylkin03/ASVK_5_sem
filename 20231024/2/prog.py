import itertools

class A:
    def slide(self, seq, n):
        for i in range(len(seq)):
            yield from itertools.islice(seq, i, i + n)

import sys
exec(sys.stdin.read())
