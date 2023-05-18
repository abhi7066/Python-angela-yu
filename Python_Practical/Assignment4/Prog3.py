# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 3.Write Python program to demonstrate the use of try, except and finally block

try:
    # Code block where an exception might occur
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ValueError:
    # Exception handler for ValueError
    print("Invalid input. Please enter valid numeric values.")

except ZeroDivisionError:
    # Exception handler for ZeroDivisionError
    print("Division by zero is not allowed.")

finally:
    # Code block that will always execute, regardless of exceptions
    print("Program execution completed.")
