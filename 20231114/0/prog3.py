from functools import wraps

def genf(f):
    @wraps(f)
    def newfun(*args):
        if not all([type(i) is int for i in args]):
            raise TypeError("Arguments must be int type")
    return newfun

@genf
def fun(a, b):
    return a**b

