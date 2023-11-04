from math import *
from itertools import combinations

class Triangle:
    def __init__(self, *args):
        a, b, c = [tuple(map(float, i)) for i in args]
        self.a = a
        self.b = b
        self.c = c

    def __bool__(self):
        ans = 1
        
        a = sqrt((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2)
        b = sqrt((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2)
        c = sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)

        if min(a, b, c) <= 0:
            ans = 0

        if a + b <= c:
            ans = 0

        if a + c <= b:
            ans = 0

        if b + c <= a:
            ans = 0

        return bool(ans)

    def __abs__(self):
        if self:
            x1, y1, x2, y2, x3, y3 = [*self.a, *self.b, *self.c]
            return abs(0.5 * ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)))
        else:
            return 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __contains__(self, other):
        self, other = other, self
        if self is other:
            return True
        if not self:
            return True
        if not other:
            return False

        t = True
        for x, y in [self.a, self.b, self.c]:
            k = [
                (other.a[0] - x)*(other.b[1] - y) - (other.b[0] - x)*(other.a[1] - y),
                (other.b[0] - x)*(other.c[1] - y) - (other.c[0] - x)*(other.b[1] - y),
                (other.c[0] - x)*(other.a[1] - y) - (other.a[0] - x)*(other.c[1] - y)
            ]
            if not (all([i < 0 for i in k]) or all([i > 0 for i in k])):
                t = False

        return t

    def __and__(self, other):
        if not self or not other:
            return False
        
        t = False
        for m0, m in combinations([self.a, self.b, self.c], 2):
            if t:
                break
            mx, my = m[0] - m0[0], m[1] - m0[1] 
            a1, b1, c1 = my, -mx, -my * m0[0] + mx * m0[1]
            for n1, n2 in combinations([other.a, other.b, other.c], 2):
                if not(min(m0[1], m[1]) >= min(n1[1], n2[1]) and min(m0[1], m[1]) <= max(n1[1], n2[1]) or min(n1[1], n2[1]) >= min(m0[1], m[1]) and min(n1[1], n2[1]) <= max(m0[1], m[1])):
                    continue
                if not(min(m0[0], m[0]) >= min(n1[0], n2[0]) and min(m0[0], m[0]) <= max(n1[0], n2[0]) or min(n1[0], n2[0]) >= min(m0[0], m[0]) and min(n1[0], n2[0]) <= max(m0[0], m[0])):
                    continue
                nx, ny = n2[0] - n1[0], n2[1] - n1[1] 
                p1 = a1 * n1[0] + b1 * n1[1] + c1
                p2 = a1 * n2[0] + b1 * n2[1] + c1
                if p1 == 0 or p2 == 0 or p1 < 0 and p2 > 0 or p1 > 0 and p2 < 0:
                    if mx == 0 and nx == 0:
                        t = True
                        break
                    if mx == 0:
                        x = m0[0]
                        if x >= min(n1[0], n2[0]) and x <= max(n1[0], n2[0]):
                            t = True
                            break
                        continue
                    if nx == 0:
                        x = n1[0]
                        if x >= min(m0[0], m[0]) and x <= max(m0[0], m[0]):
                            t = True
                            break
                        continue

                    k1, k2 = my / mx, ny / nx
                    b1, b2 = m0[1] - k1 * m0[0], n1[1] - k2 * n1[0]
                    if k1 == k2:
                        t = True
                        break
                    x = (b2 - b1) / (k1 - k2)
                    if x >= min(m0[0], m[0]) and x <= max(m0[0], m[0]) and x >= min(n1[0], n2[0]) and x <= max(n1[0], n2[0]):
                            t = True
                            break

        return t

import sys
exec(sys.stdin.read())
