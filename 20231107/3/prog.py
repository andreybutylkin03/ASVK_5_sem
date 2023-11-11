class Undead(BaseException):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

def necro(a):
    key = a % 3
    if key == 0:
        raise Skeleton
    elif key == 1:
        raise Zombie
    else:
        raise Ghoul

x, y = eval(input())
for a in range(x, y):
    try:
        necro(a)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")
