import sys

s = input()
s = s.lower()

ans = set()
siz = len(s)
if siz < 2:
    print(0)
    sys.exit()

f = s[0]
if not f.isalpha():
    f = -1
for i in range(1, siz):
    if f == -1:
        f = s[i]
        if not f.isalpha():
            f = -1
        continue

    if not s[i].isalpha():
        f = -1
        continue
        
    ans |= {f"{f}{s[i]}"}
    f = s[i]

print(len(ans))
