import sys
import pprint

ans = []
ll = 0

while (a := input()) and a:
    ans.append(list(eval(a)))
    ll += 1

if ll == 0:
    sys.exit()


lll = len(ans[0]) 

prov = [bool(len(i) == lll) for i in ans]
prov.append(ll == lll)

if all(prov):
    print("OK")
else:
    print("Not OK")
    sys.exit()

for i in range(lll):
    for j in range(i + 1, lll):
        ans[i][j], ans[j][i] = ans[j][i], ans[i][j]

for i in range(ll):
    print(*ans[i])

