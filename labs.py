'''

There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting

'''


# Get seating capacities for the three labs
a = int(input("Enter the seating capacity of L1: "))
b = int(input("Enter the seating capacity of L2: "))
c = int(input("Enter the seating capacity of L3: "))
allocated_lab = input("Enter the allocated lab for ACE training: ")

# Create a dictionary to store lab capacities
labs = {
    "L1": a,
    "L2": b,
    "L3": c
}

# Remove the allocated lab from consideration
if allocated_lab in labs:
    del labs[allocated_lab]

# Find the lab with the minimal seating capacity among the available labs
min_lab = min(labs, key=labs.get)

# Print the lab with the minimal seating capacity
print(min_lab)


'''

Sample Input:
30
40
20
L3
Sample Output:
L1
'''
