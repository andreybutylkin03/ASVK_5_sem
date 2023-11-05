class Maze:
    def __init__(self, n):
        self.n = n
        self.m = [["\u2588"] * (2 * n + 1) for i in range(2 * n + 1)]
        for i in range(1, 2 * n + 1, 2):
            for j in range(1, 2 * n + 1, 2):
                self.m[i][j] = "\u00B7"
    def __setitem__(self, item, value):
        x0, y0, y1 = item
        y0, x1 = y0.start, y0.stop
        if x0 == x1:
            for i in range(2 * (min(y0, y1) + 1), 2 * (max(y0, y1) + 1), 2):
                self.m[i][2 * x0 + 1] = value 
        elif y0 == y1:
            for i in range(2 * (min(x0, x1) + 1), 2 * (max(x0, x1) + 1), 2):
                self.m[2 * y0 + 1][i] = value 

    def __getitem__(self, item):
        t = False
        x0, y0, y1 = item
        y0, x1 = y0.start, y0.stop

        cont = [(x0, y0)]
        bew = []

        while len(cont):
            vr = cont.pop()

            if vr == (x1, y1):
                t = True
                break

            if vr in bew:
                continue

            bew.append(vr)

            if self.m[2 * vr[1]][2 * vr[0] + 1] != '\u2588' and vr[1]:
                cont.append((vr[0], vr[1] - 1))
            if self.m[2 * vr[1] + 1][2 * vr[0] + 2] != '\u2588' and vr[0] != self.n - 1:
                cont.append((vr[0] + 1, vr[1]))
            if self.m[2 * vr[1] + 2][2 * vr[0] + 1] != '\u2588' and vr[1] != self.n - 1:
                cont.append((vr[0], vr[1] + 1))
            if self.m[2 * vr[1] + 1][2 * vr[0]] != '\u2588' and vr[0]:
                cont.append((vr[0] - 1, vr[1]))

        return t
    
    def __str__(self):
        return '\n'.join([''.join(i) for i in self.m])

import sys
exec(sys.stdin.read())
