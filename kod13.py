class Calculator:

    @staticmethod
    def add(a, b):
        try:
            return a+b
        except TypeError:
            print("Wrong type(s)!")

    @staticmethod
    def div(a, b):
        try:
            return a/b
        except TypeError:
            print("Wrong type(s)!")
        except ZeroDivisionError:
            print("Division by zero!")


print(Calculator.add(4,"5"))
print(Calculator.div(4,0))

