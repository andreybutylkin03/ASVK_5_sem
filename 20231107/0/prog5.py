from math import inf

def div_ab(a, b):
    return a / b

for a, b in ((10,2),(1,0),(9,3)):
    try:
        print(div_ab(a, b))
    except ZeroDivisionError:
        print(inf)
