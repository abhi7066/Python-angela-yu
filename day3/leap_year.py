print("Welcome to Leap Year calculator")
year = int(input("Enter a Year : "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print (f"{year} is Leap year")
        else:
            print (f"{year} is not a Leap year")
    else:
        print (f"{year} is Leap year")
else:
    print (f"{year} is not Leap year")