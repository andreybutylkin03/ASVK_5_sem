def withoutsim(s):
    ans = ""
    for i in s:
        if i.isalpha():
            ans += i
        else:
            ans += ' '
    return ans

w = int(input())
d = dict()

ma = 0

while s := input():
    s = withoutsim(s)
    s = s.lower().split()

    for i in s:
        if len(i) != w:
            continue
        d.setdefault(i, 0)
        d[i] += 1
        ma = max(ma, d[i])

ans = []

for key, value in d.items():
    if value == ma:
        ans.append(key)

ans.sort()
if len(ans):
    print(*ans)
