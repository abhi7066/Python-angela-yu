# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#2. Write a program to calculate factorial of a given number using recrursion 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print("Factorial of", number, "is", factorial(number))  


# Output: Factorial of 5 is 120
