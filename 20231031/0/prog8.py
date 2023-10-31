class Rectangle:    
    rectcnt = 0
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        Rectangle.rectcnt += 1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        setattr(self, f"rect_{Rectangle.rectcnt}", 0)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}) -- {Rectangle.rectcnt}"

    def __lt__(self, elem):
        return (self.x2 - self.x1) * (self.y2 - self.y1) < (elem.x2 - elem.x1) * (elem.y2 - elem.y1)

    def __eq__(self, elem):
        return (self.x2 - self.x1) * (self.y2 - self.y1) == (elem.x2 - elem.x1) * (elem.y2 - elem.y1)

    def __mul__(self, n):
        return Rectangle(self.x1 * n, self.y1 * n, self.x2 * n, self.y2 * n)

    def __rmul__(self, n):
        return Rectangle(self.x1 * n, self.y1 * n, self.x2 * n, self.y2 * n)

    def __getitem__(self, ii):
        return [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)][ii]

    def __bool__(self):
        return True if (self.x2 - self.x1) * (self.y2 - self.y1) else False

    def __del__(self):
        print("delete", self)
        self.__class__.rectcnt -= 1
