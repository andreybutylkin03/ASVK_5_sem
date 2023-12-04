class descr:
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, obj, cls):
        def newfun(*args, **kwargs):
            print(f"{self.name}: {args}, {kwargs}")
            return self.fun(obj, *args, **kwargs)
        return newfun

    def __set_name__(self, owner, name):
        self.name = name
        

class dump(type):
    def __new__(metacls, name, parents, ns, **kwds):
        for key, val in ns.items():
            if callable(val):
                ns[key] = descr(val)
    
        return super().__new__(metacls, name, parents, ns)

import sys
exec(sys.stdin.read())
