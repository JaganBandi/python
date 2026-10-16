class Calculator:

    @staticmethod
    def add(a, b):
        print("add:", a + b)

    @staticmethod
    def sub(a, b):
        print("Sub:", a - b)

    @staticmethod
    def mul(a, b):
        print("Mul:", a * b)

    @staticmethod
    def div(a, b):
        print("Div:", a / b)

    @staticmethod
    def square(a):
        print("Square:", a ** 2)


Calculator.add(10, 40)
Calculator.sub(500, 220)
Calculator.mul(42, 30)
Calculator.div(200, 5)
Calculator.square(25)