class Factorial:
    def __init__(self, num: int):
        """
        num: int, target for factorial
        """
        self._target = num
    
    def __call__(self):
        return self.play()
    
    def play(self):
        if self._target == 1:
            return 1
        else:
            return self._target * factorial(self._target-1)

def factorial(num):
    return Factorial(num)()

if __name__=='__main__':
    print(factorial(11))
