class Desc:
    def __get__(self, obj, cls):
        print("GET", obj, cls)
        return obj._val
    def __set__(self, obj, val):
        obj._val = val
    def __delete__(self, obj):
        obj._val = None

class F00:
    x = Desc()


