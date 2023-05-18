# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 1.Write Python program to demonstrate the following:
#   1.SyntaxError
#   2.TypeError
#   3.IndexError
#   4.ValueError
#   5.ZeroDivisionError
#   6.fileNotFound

# SyntaxError
print("Hello, World!"  # Missing closing parenthesis

# TypeError
number = 10
text = "Hello"
result = number + text  # Adding int and str

# IndexError
my_list = [1, 2, 3]
print(my_list[3])  # Accessing index out of range

# ValueError
user_input = input("Enter a number: ")
number = int(user_input)  # Converting non-numeric input to int

# ZeroDivisionError
numerator = 10
denominator = 0
result = numerator / denominator  # Division by zero

# FileNotFoundError
file_path = "nonexistent_file.txt"
with open(file_path, "r") as file:  # Opening a nonexistent file
    content = file.read()
