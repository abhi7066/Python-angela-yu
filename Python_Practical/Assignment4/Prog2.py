# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 2.Write Python program to raise user defined exception

class MyCustomException(Exception):
    pass

def divide_numbers(a, b):
    if b == 0:
        raise MyCustomException("Division by zero is not allowed.")
    return a / b

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = divide_numbers(numerator, denominator)
    print("Result:", result)

except MyCustomException as e:
    print("Custom Exception Raised:", e)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")

except Exception as e:
    print("An error occurred:", e)
