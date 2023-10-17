from collections import Counter

s = input().split()
c = Counter(s)
for key, value in c.items():
    print(key, value, sep=' - ')
