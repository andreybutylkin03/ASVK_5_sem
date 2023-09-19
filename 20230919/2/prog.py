ans = 0
while ans <= 21 and (n := input()) and int(n) > 0:
    ans += int(n)
else:
    if int(n) <= 0:
        print(n)
    elif ans > 21:
        print(ans)
