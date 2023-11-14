from functools import wraps

def genf(f):
    @wraps(f)
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@genf
def fun(a, b):
    return a**b

