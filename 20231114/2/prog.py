class Num:
    def __init__(self):
        self.obj_buf = set()

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, cls):
        if obj not in self.obj_buf:
            return 0
        return getattr(obj, self.private_name)

    def __set__(self, obj, val):
        self.obj_buf.add(obj)

        if 'real' in dir(val):
            setattr(obj, self.private_name, val.real)
        else:
            setattr(obj, self.private_name, len(val))

    def __delete__(self, obj):
        if obj in self.obj_buf:
            setattr(obj, self.private_name, None)

import sys
exec(sys.stdin.read())
