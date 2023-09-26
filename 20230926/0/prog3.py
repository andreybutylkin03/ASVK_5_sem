n = list(range(5, 16))
s = list(map(lambda x: chr(x), range(ord('a'), ord('k') + 1)))
n[4:8] = s[-5:]
print(*n[-1:len(n) // 2 - 1: -2])
