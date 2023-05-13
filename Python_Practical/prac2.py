# Reverse a string
def reverse_string(string):
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string

# Count vowels and consonants in a string
def count_vowels_and_consonants(string):
  vowels = ["a", "e", "i", "o", "u"]
  consonants = []
  for letter in string:
    if letter in vowels:
      vowels.append(letter)
    else:
      consonants.append(letter)
  return len(vowels), len(consonants)

# Count the number of letters in a word
def count_letters_in_word(word):
  return len(word)

# Convert lower letter to upper and upper letter to lower in a string
def convert_case(string):
  converted_string = ""
  for letter in string:
    if letter.islower():
      converted_string += letter.upper()
    else:
      converted_string += letter.lower()
  return converted_string

# Count lower, upper, numeric and special characters in a string
def count_characters(string):
  lower_case_count = 0
  upper_case_count = 0
  numeric_count = 0
  special_character_count = 0
  for letter in string:
    if letter.islower():
      lower_case_count += 1
    elif letter.isupper():
      upper_case_count += 1
    elif letter.isdigit():
      numeric_count += 1
    else:
      special_character_count += 1
  return lower_case_count, upper_case_count, numeric_count, special_character_count


# Reverse a string
string = "Hello World!"
reversed_string = reverse_string(string)
print("The reversed string is:", reversed_string)

# Count vowels and consonants in a string
string = "Hello World!"
vowels_count, consonants_count = count_vowels_and_consonants(string)
print("The number of vowels in the string is:", vowels_count)
print("The number of consonants in the string is:", consonants_count)

# Count the number of letters in a word
word = "Hello"
letter_count = count_letters_in_word(word)
print("The number of letters in the word is:", letter_count)

# Convert lower letter to upper and upper letter to lower in a string
string = "Hello World!"
converted_string = convert_case(string)
print("The converted string is:", converted_string)

# Count lower, upper, numeric and special characters in a string
string = "Hello World!"
lower_case_count, upper_case_count, numeric_count, special_character_count = count_characters(string)
print("The number of lower case characters in the string is:", lower_case_count)
print("The number of upper case characters in the string is:", upper_case_count)
print("The number of numeric characters in the string is:", numeric_count)
print("The number of special characters in the string is:", special_character_count)
