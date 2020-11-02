

from calculator.sub import sub
from calculator.add import add
from calculator.mul import mul
from calculator.div import div
from calculator.square import square
from calculator.square_root import square_root

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = sub(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = mul(a, b)
        return self.result

    def divide(self, a, b):
        self.result = div(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = square_root(a)
        return self.result
