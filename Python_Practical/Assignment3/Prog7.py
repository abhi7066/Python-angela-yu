# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#7. Write Python program to read List of Dictionaries from File

import json

def read_list_of_dictionaries(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

filename = 'filename.txt'
list_of_dicts = read_list_of_dictionaries(filename)
print("List of dictionaries:", list_of_dicts)
