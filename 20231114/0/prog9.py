class C:
    def __init__(self):
        self._val = 0
    @property
    def age(self):
        if self._val == 42:
            print("Secret value!")
            return -1
        return self._val

    @age.setter
    def age(self, val):
        self._val = val
