def type_pr(typee):
    def decorator(fun):
        def newfun(*args):
            if not all([isinstance(i, typee) for i in args]):
                raise TypeError
            else:
                return fun(*args)
        return newfun
    return decorator

@type_pr(int)
def simplefun(a, b):
    return 2 * a + b

