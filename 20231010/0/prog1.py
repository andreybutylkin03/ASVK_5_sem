from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)


print(multiplier(*(input().split(',')), float))
print(multiplier(*(input().split(',')), Decimal))
print(multiplier(*(input().split(',')), Fraction))
