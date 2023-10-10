from decimal import Decimal, getcontext

def esum(N, one):
    Type = type(one)
    e = Type('0')
    n = Type('1')
    for i in range(0, N + 1):
        e += Type(1)/n
        n *= Type(f"{i + 1}")

    return e

print(esum(100, Decimal(1)))

