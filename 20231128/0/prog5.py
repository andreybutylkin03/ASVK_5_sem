ss = input().split()

class CONST:
    f = ss[0]
    s = ss[1]
    t = ss[2]

while s := input():
    match s.split():
        case [CONST.f, *args] if "yes" in args:
            print("FIRST")
        case [CONST.s]:
            print("SECOND")
        case [CONST.t, *args, CONST.f]:
            print("THIRD")
