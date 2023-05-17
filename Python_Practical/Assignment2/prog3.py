# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 3. Write a program to create decorators and generators

# Decorator Example
def uppercase_decorator(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())  # Output: HELLO WORLD


# Generator Example
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib), end=" ")
print()



  # Output: 0 1 1 2 3 5 8 13 21 34