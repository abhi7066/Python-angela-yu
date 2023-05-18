# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 4.Write Python program to demonstrate default except block

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

except:
    # Default exception handler for any other exception
    print("An error occurred.")

finally:
    # Code block that will always execute, regardless of exceptions
    print("Program execution completed.")
