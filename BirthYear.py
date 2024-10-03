'''

Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.

'''
# Get the last two digits of the birth year
birth_year = int(input("Enter the last two digits of your birth year: "))
# Get the last two digits of the current year
current_year = int(input("Enter the last two digits of the current year: "))

# Calculate age
age = current_year - birth_year

# Adjust for cases where the birth year is later in the century
if age < 0:
    age += 100

# Print the user's current age
print(age)


'''

Sample Input:
62
00
Sample Output:
38

'''
