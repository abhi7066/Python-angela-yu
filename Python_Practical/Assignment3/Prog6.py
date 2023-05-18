# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#6. Write Python program to Count number of lines in a text file in Python

def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    return count

filename = 'filename.txt'
line_count = count_lines(filename)
print("Number of lines:", line_count)
