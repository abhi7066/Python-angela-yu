# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


# 10.Write Python program to merge two files into a third file

def merge_files(file1, file2, merged_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    merged_content = content1 + '\n' + content2

    with open(merged_file, 'w') as f:
        f.write(merged_content)

    print("Files merged into", merged_file)


file1 = 'source.txt'
file2 = 'destination.txt'
merged_file = 'merged_file.txt'
merge_files(file1, file2, merged_file)
