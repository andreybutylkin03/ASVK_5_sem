import pickle

class SerCls:
    lst = []
    dct = dict()
    num = 1
    st = ""

    def __init__(self, **kargs):
        for key, val in kargs.items():
            setattr(self, key, val)

ser = SerCls(lst=[1, 2, 3], dct={"1":11}, num=100500, st="aboba")
res = pickle.dumps(ser)
print(res)

del ser
ser1 = pickle.loads(res)

