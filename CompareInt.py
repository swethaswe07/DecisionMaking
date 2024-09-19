'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"

'''

# Program to compare two integers

# Get input from the user
x = int(input("Enter the first number (x):\n"))
y = int(input("Enter the second number (y):\n"))

# Compare the two integers and print the result
if x == y:
    print(f"{x} and {y} are equal")
elif x > y:
    print(f"{x} greater than {y}")
else:
    print(f"{x} less than {y}")


'''

Enter the first number (x):
6
Enter the second number (y):
8

output

6 less than 8

'''
