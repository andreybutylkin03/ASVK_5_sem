class Num:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, cls):
        try:
            return getattr(obj, self.private_name)
        except Exception:
            return 0

    def __set__(self, obj, val):
        if 'real' in dir(val):
            setattr(obj, self.private_name, val.real)
        else:
            setattr(obj, self.private_name, len(val))

    def __delete__(self, obj):
        try:
            setattr(obj, self.private_name, None)
        except Exception:
            pass

import sys
exec(sys.stdin.read())
