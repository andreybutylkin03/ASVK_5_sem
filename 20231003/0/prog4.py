def solve(f, g):
    def h(x):
        return f(x) + g(x)
    return h

#print(solve(lambda x: x + 2, lambda x: x + 1)(1)) 
