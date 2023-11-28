class Doubeleton(type):
    _instance_1 = None
    _instance_2 = None
    _flag = True

    def __call__(cls, *args, **kw):
        if cls._instance_1 is None:
            cls._instance_1 = super().__call__(*args, **kw)
        elif cls._instance_2 is None:
            cls._instance_2 = super().__call__(*args, **kw)
        
        cls._flag = not cls._flag
        return cls._instance_1 if cls._flag else cls._instance_2
