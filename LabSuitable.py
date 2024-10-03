'''

 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting

'''

# Get seating capacities for the three labs and the number of students
x = int(input("Enter the seating capacity of L1: "))
y = int(input("Enter the seating capacity of L2: "))
z = int(input("Enter the seating capacity of L3: "))
n = int(input("Enter the number of students: "))

# Initialize variables to track the best lab and its capacity
best_lab = None
max_capacity = -1

# Check each lab's capacity
if x >= n and x > max_capacity:
    best_lab = "L1"
    max_capacity = x
if y >= n and y > max_capacity:
    best_lab = "L2"
    max_capacity = y
if z >= n and z > max_capacity:
    best_lab = "L3"
    max_capacity = z

# Print the suitable lab
if best_lab:
    print(best_lab)
else:
    print("No suitable lab available")

'''

Sample Input:
30
40
20
25
Sample Output:
L1

'''
