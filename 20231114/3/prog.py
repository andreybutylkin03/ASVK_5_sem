import string
from dataclasses import dataclass

class Alpha:
    __slots__ = list(string.ascii_lowercase)
    
    def __init__(self, **kargs):
        for key, value in kargs.items():
            setattr(self, key, value)

    def __str__(self):
        ans = []
        for i in string.ascii_lowercase:
            if hasattr(self, i):
                ans.append(f"{i}: {getattr(self, i)}")
        return ', '.join(ans)

class AlphaQ:
    __s = set(string.ascii_lowercase)

    def __init__(self, **kargs):
        for key, value in kargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        ans = []
        for i in string.ascii_lowercase:
            if self.__dict__.get(i, None) is not None:
                ans.append(f"{i}: {self.__dict__[i]}")
        return ', '.join(ans)

    def __setattr__(self, attr, val):
        if attr in __class__.__s:
            self.__dict__[attr] = val
        else:
            raise AttributeError

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        raise AttributeError

import sys
exec(sys.stdin.read())
