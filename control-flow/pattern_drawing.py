size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Newline after each row
    row += 1
