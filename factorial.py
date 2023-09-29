class Factorial :
    def __init__(self, num: int) :
        """
        Initialize target number with the number given by user.

        Attributes :
            num (int): target number to do factorial
        """
        self.num = num

    def start(self) :
        """
        Print out the result of factorial(num).
        Factorial is a process of multiplying numbers from 1 to num sequentially.
        """
        result = 1
        for i in range(2, self.num+1) :
            result *= i
        print(result)
    
if __name__ == '__main__' :
    fact = Factorial(1)
    fact.start()