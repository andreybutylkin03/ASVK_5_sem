import collections

class DivStr(collections.UserString):
    def __init__(self, st='', step=1, kol=1):
        super().__init__(st)
        self.step = step
        self.st = st
        self.si = len(st)
        self.i = 0
        self.kol = self.si

    def __floordiv__(self, num):
        self.kol = num
        return DivStr(self.st, self.si // self.kol)

    def __mod__(self, num):
        vr = divmod(self.si, num)
        return DivStr('') if vr[1] == 0 else DivStr(self.st[-vr[1]:])

    def __iter__(self):
        self.i = 0
        self.kol = 0 if self.step == 0 else self.si // self.step
        return self

    def __next__(self):
        if self.kol == 0:
            raise StopIteration
        else:
            self.kol -= 1
            self.i += self.step
            return self.st[self.i - self.step: self.i]

import sys
exec(sys.stdin.read())
