def foo(a, b):
    def solve(x):
        return a * x + b

    return solve

#print(foo(1, 2)(3))
