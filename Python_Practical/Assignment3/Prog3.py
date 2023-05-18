# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A



#3. Write Python program to Get number of characters, words, spaces and lines in a file

filename = 'filename.txt'
characters = words = spaces = lines = 0

with open(filename, 'r') as file:
    for line in file:
        lines += 1
        characters += len(line)
        words += len(line.split())
        spaces += line.count(' ')

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of spaces:", spaces)
print("Number of lines:", lines)
