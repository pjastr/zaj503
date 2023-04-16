try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter a number: "))
    print("suma x/y =", x/y)
except ValueError:
    print("This is no valid number.")
except ZeroDivisionError:
    print("Division by zero!!!")
except Exception:
    print("Other error")
