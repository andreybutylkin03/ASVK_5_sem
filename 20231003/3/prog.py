from math import *

def Calc(s, t, u):
    def ans(a, xxx = lambda x: eval(s), yyy = lambda x: eval(t)):
        x = xxx(a)
        y = yyy(a)
        return eval(u)

    return ans

print(Calc(*eval(input()))(eval(input())))
