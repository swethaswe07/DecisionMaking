'''

Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”

'''

# Program to check whether a character is a vowel or consonant

# Get input from the user
char = input("Enter a character:\n").lower()  # Convert to lowercase for uniformity

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")


'''

Enter a character:
e

output

Vowel


'''
