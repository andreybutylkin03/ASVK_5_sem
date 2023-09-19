def sumof(a):
    ans = 0
    while a:
        ans += a % 10
        a //= 10

    return ans

n = int(input())

i, j = n, n

while i <= n + 2:
    j = n
    while j <= n + 2:
        ans = i * j
        print(i, '*', j, '=', end=' ')
        if sumof(ans) == 6:
            print(':=)', end=' ')
        else:
            print(ans, end=' ')

        j += 1

    i += 1
    print()

