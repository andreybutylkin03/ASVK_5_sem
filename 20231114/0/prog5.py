class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            Sender.report(i)

class Sender:
    ff = "Greetings!"
    @classmethod
    def report(cls, arg):
        print(cls.ff)
        cls.ff = "Get away!"
