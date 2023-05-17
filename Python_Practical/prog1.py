def sum_list(list1):
  sum = 0
  for item in list1:
    sum += item
  return sum

def get_largest_number(list1):
  largest = list1[0]
  for item in list1:
    if item > largest:
      largest = item
  return largest

def remove_duplicates(list1):
  seen = set()
  new_list = []
  for item in list1:
    if item not in seen:
      seen.add(item)
      new_list.append(item)
  return new_list

def separate_positive_negative(list1):
  positive_list = []
  negative_list = []
  for item in list1:
    if item > 0:
      positive_list.append(item)
    else:
      negative_list.append(item)
  return positive_list, negative_list

def filter_even_odd(list1):
  even_list = []
  odd_list = []
  for item in list1:
    if item % 2 == 0:
      even_list.append(item)
    else:
      odd_list.append(item)
  return even_list, odd_list



# Function Calling
list1 = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]

sum = sum_list(list1)
print("The sum of the items in the list is:", sum)

largest = get_largest_number(list1)
print("The largest number in the list is:", largest)

new_list = remove_duplicates(list1)
print("The list after removing duplicates is:", new_list)

positive_list, negative_list = separate_positive_negative(list1)
print("The list of positive numbers is:", positive_list)
print("The list of negative numbers is:", negative_list)

even_list, odd_list = filter_even_odd(list1)
print("The list of even numbers is:", even_list)
print("The list of odd numbers is:", odd_list)
