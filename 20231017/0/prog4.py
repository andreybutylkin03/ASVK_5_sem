s = input().split()
d = dict()
for i in s:
    d.setdefault(i, 0)
    d[i] += 1
for key, value in d.items():
    print(key, value, sep=' - ')
