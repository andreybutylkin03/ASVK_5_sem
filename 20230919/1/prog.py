a, b, c = '-', '-', '-'

n = int(input())

if n % 25 == 0:
    if n % 2:
        b = '+'
    else:
        a = '+'
if n % 8 == 0:
    c = '+'

print('A', a, 'B', b, 'C', c)
