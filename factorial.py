class Factorial:
    def __init__(self):
        pass
    def start(self, n):
        if n == 1:
            return 1
        else:
            return self.start(n-1)*n
