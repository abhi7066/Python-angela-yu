for i in range(4):
    for j in range (i+1):
        print(j+1, end=" ")
    print()
print()

for i in range(4,0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
print()

ch=65
for i in range(0, 6):
    for j in range(i):
        print(chr(ch), end=" ")
        ch+=1

    print()