s = input()

a, b = eval(input())
print(eval(s, {"x": a, 'y': b}), eval(s, {'x': b, 'y': a}), sep='\n')
