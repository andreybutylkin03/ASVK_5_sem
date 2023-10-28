import itertools

class A:
    def fib(self, m, n):
        def vs(a=1, b=0):
            while True:
                yield a
                a, b = a + b, a

        return itertools.islice(vs(), m, m + n)

import sys
exec(sys.stdin.read())
