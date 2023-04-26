#This will print abitrary variable
def my_function(arg1, *arg2):
    for x in arg2:
        print(x)
    print(arg1)
    print(arg2)

my_function(6,78,8,0)