from collections import Counter

print(*[key for key, value in Counter(input().split()).items()])
