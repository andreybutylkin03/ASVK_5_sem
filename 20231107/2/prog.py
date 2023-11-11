class InvalidInput(BaseException):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput

    try:
        (x1, y1), (x2, y2), (x3, y3) = map(lambda x: (float(x[0]), float(x[1])), [(x1, y1), (x2, y2), (x3, y3)])
        s = abs(0.5 * ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)))
        proxy = 1 / s
    except:
        raise BadTriangle

    return s

while True:
    try:
        s = triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{s:.2f}")
        break
