def solve(a, b):
    if isinstance(a, tuple) or isinstance(a, list):
        ans = []
        for i in a:
            if i not in b:
                ans.append(i)

        return type(a)(ans)
    else:
        return a - b

print(solve(*eval(input())))
