class A():
    def __init__(self, var):
        self.var = var

    def __add__(self, num):
        return self.__class__(self.var + num)

class B(A):
    def __str__(self):
        return f"{self.var}"
