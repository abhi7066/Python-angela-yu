
#9. Write Python program to reverse the content of a file and store it in another file

def reverse_file_content(source_file, destination_file):
    with open(source_file, 'r') as source:
        lines = source.readlines()

    reversed_lines = reversed(lines)

    with open(destination_file, 'w') as destination:
        destination.writelines(reversed_lines)

    print("File content reversed and stored in", destination_file)


source_file = 'filename.txt'
destination_file = 'reversed_filename.txt'
reverse_file_content(source_file, destination_file)
