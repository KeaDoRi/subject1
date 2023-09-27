class Factorial:
    def __init__(self, number):
        self.number = number
    def factorial(self):
        result = 1
        for item in range(1, self.number+1, 1):
            result *= item
        return print(result)


test = Factorial(10)

test.factorial()



