# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#2. Write Python program to read character by character from a file

with open('filename.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        print(char)
