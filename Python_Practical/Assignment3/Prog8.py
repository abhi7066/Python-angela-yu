# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#8. Write Python program to Append content of one text file to another

def append_files(source_file, destination_file):
    with open(source_file, 'r') as source:
        source_data = source.read()
    with open(destination_file, 'a') as destination:
        destination.write(source_data)
    print("Content is appended!")

source_file = 'source.txt'
destination_file = 'destination.txt'
append_files(source_file, destination_file)

