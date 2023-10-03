def Pareto(*a):
    n = len(a)
    ans = []
    for i in range(n):
        flag = True
        for j in range(n):
            if i == j:
                continue

            if a[i][0] < a[j][0] and a[i][1] <= a[j][1] or a[i][0] <= a[j][0] and a[i][1] < a[j][1]:
                flag = False

        if flag:
            ans.append(a[i])

    return ans

ans = tuple(Pareto(*tuple(eval(input()))))
print(ans)
