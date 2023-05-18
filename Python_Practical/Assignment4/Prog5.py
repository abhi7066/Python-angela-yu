# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 5.Write Python program to handle multiple exceptions in single except block 

try:
    # Code block where an exception might occur
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    result = numerator / denominator
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    # Exception handler for multiple exceptions
    print("An error occurred. Please enter valid numeric values and avoid division by zero.")

finally:
    # Code block that will always execute, regardless of exceptions
    print("Program execution completed.")
