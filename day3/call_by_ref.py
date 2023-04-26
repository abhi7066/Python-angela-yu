# Function definition is here
def changeme( a ):
   "This changes a passed list into this function"
   a.append([1,2,3,4]);
   print ("Values inside the function: ", a)
   print(id(a))


# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

print(id(mylist))