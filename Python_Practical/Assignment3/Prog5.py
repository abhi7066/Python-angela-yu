# Name : Abhishek Dethe
# Roll No: 2201037
# Div  A


#5. Write Python program to Find ‘n’ Character Words in a Text File

def find_n_character_words(filename, n):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            line_words = line.split()
            for word in line_words:
                if len(word) == n:
                    words.append(word)
    return words

filename = 'filename.txt'
n = 4
n_character_words = find_n_character_words(filename, n)
print("Words with", n, "characters:", n_character_words)
