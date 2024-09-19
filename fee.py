'''
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.

Student Type	               Student Type Code     	Fee Details
Merit Seat Day Scholar	           MSDS	            Tuition fee + Bus fee
Merit Seat Hosteller	            MSH	              Tuition fee + Hostel fee
Management Seat Day Scholar      	MGSDS            	150% of Tuition fee + Bus fee
Management Seat Hosteller	         MGSH	        150% of Tuition fee + Hostel fee

Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting

'''


# Program to calculate the fee amount for a student

# Input the student type
student_type = input("Enter the student type (MSDS, MSH, MGSDS, MGSH):\n").strip()
# Input the tuition fee
tuition_fee = float(input("Enter the tuition fee:\n"))
# Input the bus or hostel fee
additional_fee = float(input("Enter the bus fee or hostel fee:\n"))

# Initialize total fee variable
total_fee = 0.0

# Determine the fee based on student type
if student_type == "MSDS":
    total_fee = tuition_fee + additional_fee  # Tuition + Bus fee
elif student_type == "MSH":
    total_fee = tuition_fee + additional_fee  # Tuition + Hostel fee
elif student_type == "MGSDS":
    total_fee = 1.5 * tuition_fee + additional_fee  # 150% of Tuition + Bus fee
elif student_type == "MGSH":
    total_fee = 1.5 * tuition_fee + additional_fee  # 150% of Tuition + Hostel fee
else:
    print("Invalid student type")
    exit()


'''
Enter the student type (MSDS, MSH, MGSDS, MGSH):
MSH
Enter the tuition fee:
40000
Enter the bus fee or hostel fee:
50000

output
Enter the student type (MSDS, MSH, MGSDS, MGSH):
MSH
Enter the tuition fee:
40000
Enter the bus fee or hostel fee:
50000
'''

# Print the total fee amount formatted to 2 decimal places
print(f"{total_fee:.2f}")
