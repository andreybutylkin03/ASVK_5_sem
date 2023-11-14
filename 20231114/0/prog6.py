class Desc:
    def __get__(self, obj, cls):
        print("GET", obj, cls)
        return obj._val
    def __set__(self, obj, val):
        obj._val = val

class C:
    field = Desc()

