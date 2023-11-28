import inspect

class C:
    a: int
    def __init__(self, var):
        if isinstance(var, inspect.get_annotations()['a']):
            self.a = var
        else:
            raise TypeError
