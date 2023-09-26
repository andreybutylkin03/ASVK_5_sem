b, e = eval(input())

a = list(range(b, e + 1))

print(*[i for i in a if i % 2 and '3' not in str(i)])
