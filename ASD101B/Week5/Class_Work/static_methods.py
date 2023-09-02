import math

# Static methods vs instance methods
# A static method can be called without the use of an object

class Calculator:

    # Create AddNumbers static method by using @staticmethod decorator
    @staticmethod
    def AddNumbers(x, y):
        return x + y
    
    @staticmethod
    def multiplyNumbers(x, y):
        return x * y


ans = Calculator.AddNumbers(12, 14)
print(f'The answer is {ans}')

multAns = Calculator.multiplyNumbers(3, 5)
print(multAns)
