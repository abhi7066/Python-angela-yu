# create a sample dictionary
sample_dict = {"apple": 3, "banana": 2, "orange": 4, "kiwi": 1}

# 1. Check whether a given key exists in a dictionary or not.
key = "banana"
if key in sample_dict:
    print(f"{key} exists in the dictionary.")
else:
    print(f"{key} does not exist in the dictionary.")

# 2. Iterate over dictionary items using for loop.
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# 3. Concatenate two dictionaries to create one.
dict1 = {"apple": 3, "banana": 2}
dict2 = {"orange": 4, "kiwi": 1}
concat_dict = {**dict1, **dict2}
print(concat_dict)

# 4. Sum all the values of a dictionary.
total = sum(sample_dict.values())
print(f"The sum of all values in the dictionary is {total}.")

# 5. Get the maximum and minimum value of dictionary.
max_value = max(sample_dict.values())
min_value = min(sample_dict.values())
print(f"The maximum value in the dictionary is {max_value} and the minimum value is {min_value}.")
