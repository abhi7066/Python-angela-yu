import re

def Validate_url(str):
    p = re.compile("^https?://[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$")
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


def Validate_email(str):
    p = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


def Validate_password(str):
    p = re.compile("^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-={}]).{8,}$")
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


str1 = "https://instagram.com"
if(Validate_url(str1)):
    print("url is valid.")
else:
    print("url is invalid.")

str1 = "abc@gamail.com"
if(Validate_email(str1)):
    print("email is valid.")
else:
    print("email is invalid.")

str1 = "Pass@123"
if(Validate_password(str1)):
    print("Password is valid.")
else:
    print("Password is invalid.")



