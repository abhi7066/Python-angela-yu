# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A



# 1.Write a program to demonstrate Nested function
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

result = outer_function(5)
print(result(10))  


# Output: 15
