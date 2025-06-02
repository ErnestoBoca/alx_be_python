size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    for j in range(size):
        print("x", end="")
    print()
    i = i + 1