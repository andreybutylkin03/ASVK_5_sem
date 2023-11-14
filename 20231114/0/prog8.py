class C:
    def __init__(self):
        self._val = None

    @property
    def x(self):
        return self._val

    @x.setter
    def x(self, val):
        self._val = val


