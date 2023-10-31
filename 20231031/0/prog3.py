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
