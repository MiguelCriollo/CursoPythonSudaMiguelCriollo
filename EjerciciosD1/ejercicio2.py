class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


if __name__ == '__main__':
    num1 = 8
    num2 = 4
    print(f"{num1} + {num2} = {Calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {Calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {Calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {Calculator.divide(num1, num2)}")
