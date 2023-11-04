class Omnibus:
    bufcopy = []
    bufattr = []

    def __init__(self):
        Omnibus.bufcopy.append(self)
        vr = Omnibus.bufcopy[0]
        if vr != self:
            for i in Omnibus.bufattr:
                object.__setattr__(self, i, [object.__getattribute__(vr, i)[0], 0])

    def __getattribute__(self, attr):
        if attr in Omnibus.bufattr:
            return object.__getattribute__(self, attr)[0]
        else:
            return 0

    def __setattr__(self, attr, value):
        t = False
        if attr not in Omnibus.bufattr:
            Omnibus.bufattr.append(attr)
            t = True
        con = True
        if not t:
            if object.__getattribute__(self, attr)[1] == 1:
                con = False
        if con:
            for i in Omnibus.bufcopy:
                if t:
                    object.__setattr__(i, attr, [0, 0])
                vr = object.__getattribute__(i, attr)
                object.__setattr__(i, attr, [vr[0] + 1, vr[1]])
            
            vr = object.__getattribute__(self, attr)
            object.__setattr__(self, attr, [vr[0], 1])

    def __delattr__(self, attr):
        if attr in Omnibus.bufattr:
            if object.__getattribute__(self, attr)[1] == 1:
                vr = object.__getattribute__(self, attr)
                object.__setattr__(self, attr, [vr[0], 0])
                for i in Omnibus.bufcopy:
                    vr = object.__getattribute__(i, attr)
                    object.__setattr__(i, attr, [vr[0] - 1, vr[1]])

import sys
exec(sys.stdin.read())
