import math

class Calculator:
    def __init__(self, n):
        self.n = n
        print("Calculation is started")

    def square(self):
        print(f"The Square is {self.n * self.n}")

    def cube(self):
        print(f"The Cube is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The Square Root is {math.sqrt(self.n)}")

    @staticmethod
    def greet():
        print("Good Morning ")
number = Calculator(4)
number.greet()
number.cube()
number.square()
number.square_root()
0