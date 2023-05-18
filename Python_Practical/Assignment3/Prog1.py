# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#1. Write Python program to read file word by word

with open('filename.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            print(word)
