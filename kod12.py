def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("wrong type!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide("2", "4")