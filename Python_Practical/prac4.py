# 1. First 10 natural numbers
print("First 10 natural numbers: ", end="")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. First 10 even numbers in reverse order
print("First 10 even numbers in reverse order :", end="")
for i in range(20, 0, -2):
    print(i, end=" ")
print()

# 3. Table of a number accepted from user
num = int(input("Enter a number: "))
print(f"Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 4. First 10 prime numbers
print("First 10 prime numbers: ", end="")
count = 0
num = 2
while count < 10:
    is_prime = True
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
print()
