import sys

n, m = 0, 0
g, w = 0, 0

data = sys.stdin.readlines()

for s in data:
    if not n:
        m = len(s)
    n += 1
    gg = [1 for i in s if i == '.']
    ww = [1 for i in s if i == '~']
    g += sum(gg)
    w += sum(ww)

n -= 2
m -= 2
neww = w + g % n
newg = g - g % n

print('#' * (n + 2))
for i in range(m):
    if newg:
        print(f"#{'.' * n}#")
        newg -= n
    elif neww:
        print(f"#{'~' * n}#")
        neww -= n
print('#' * (n + 2))

if g == w:
    print(f"{'.' * 20} {g}/{g + w}")
    print(f"{'~' * 20} {w}/{g + w}")
elif g < w:
    print(f"{'.' * round(g * 20 / w)}{' ' * (21- round(g * 20 / w) + len(str(w)) - len(str(g)))}{g}/{g + w}")
    print(f"{'~' * 20} {w}/{g + w}")
else:
    print(f"{'.' * 20} {g}/{g + w}")
    print(f"{'~' * round(w * 20 / g)}{' ' * (21- round(w * 20 / g) + len(str(g)) - len(str(w)))}{w}/{g + w}")
