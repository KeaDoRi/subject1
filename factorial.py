from functools import cache


class Factorial:  # pep8 guide
    def __init__(self, num: int):
        """
        num: int, target for factorial
        """
        self._target = num

    def __call__(self):
        return self.start()

    def start(self):
        """
        if target == 1, return 1
        otherwise target * factorial(target-1)
        :return:
            target's factorial
        """
        if self._target == 1:
            return 1
        else:
            return self._target * factorial(self._target - 1)


@cache
def factorial(num):
    return Factorial(num)()


if __name__ == '__main__':
    print(factorial(11))
