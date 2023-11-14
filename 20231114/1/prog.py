def objcount(cls):
    class obje(cls):
        cls.counter = 0

        def __init__(self, *args, **kargs):
            super().__init__(*args, **kargs)
            self.__class__.counter += 1

        def __del__(self):
            if '__del__' in dir(cls):
                super().__del__()
            self.__class__.counter -= 1

    return obje
            
import sys
exec(sys.stdin.read())
