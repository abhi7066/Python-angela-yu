def Add(*args):
    result = sum(args)
    print("The sum is:", result)

def Mul(*args):
    result = 1
    for num in args:
        result *= num
    print("The product is:", result)

def Sub(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    print("The difference is:", result)

def Div(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    print("The quotient is:", result)


Add(1, 2, 3)
Mul(1, 2, 3)
Sub(10, 5, 3)
Div(10, 2, 5)



#                   OUTPUT
#   The sum is: 6
#   The product is: 6
#   The difference is: 2
#   The quotient is: 1.0"""