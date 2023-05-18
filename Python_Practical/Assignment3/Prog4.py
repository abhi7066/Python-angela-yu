# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#4. Write Python program to Count the Number of occurrences of a key-value pair in a text file

def count_key_value(filename, key, value):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            for item in data:
                if item == key:
                    next_item = data[data.index(item) + 1]
                    if next_item == value:
                        count += 1
    return count

filename = 'filename.txt'
key = 'key'
value = 'value'
occurrences = count_key_value(filename, key, value)
print("Number of occurrences:", occurrences)
