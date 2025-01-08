"""
      1
    2   3
  4   5   6
7   8   9  10

""" 
#print the following pattern

"""n=10
Current=1
rows=4

for i in range(1,rows+1):
    print(" "* (rows-1)* 2, end="")

    for j in range(i):
        if Current<=n:
            print(Current, end="   ")
            Current+=1

    print()"""

n = 15  # Total numbers to print
current = 1  # Start number
rows = 5  # Total rows in the pattern

# Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces for alignment
    print(" " * (rows - i), end="")
    
    # Print numbers in the current row with spacing
    for j in range(i):
        if current <= n:
            print(current, end="   ")  # Add 3 spaces between numbers
            current += 1
    
    # Move to the next row
    print()


