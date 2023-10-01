class factorial : 
    def __init__(self, num):
        self.num = num

    def func_num1(self):
        print(self.num)
    
    def func_num2(self):
        return self.num
    
    def start(self):
        self.factorial()

f = factorial(3)

# =================

class Factorial:
    def __init__(self):
        pass
    def start(self, n):
        if n == 1:
            return 1
        else:
            return start(n-1) * n


