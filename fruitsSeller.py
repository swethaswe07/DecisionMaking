'''
 A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.

'''


# Program to determine profit or loss for a fruit seller

# Input the total cost for a dozen bananas
cost_per_dozen = float(input("Enter the total cost for a dozen bananas (X):\n"))
# Input the selling price of one banana
selling_price_per_banana = float(input("Enter the selling price of one banana (Y):\n"))

# Calculate total selling price for a dozen bananas
total_selling_price = selling_price_per_banana * 12

# Calculate profit or loss
profit_loss = total_selling_price - cost_per_dozen

# Output the result
if profit_loss > 0:
    print(f"Profit : Rs.{profit_loss:.2f}")
elif profit_loss < 0:
    print(f"Loss : Rs.{abs(profit_loss):.2f}")
else:
    print("No Profit No Loss")



'''

Enter the total cost for a dozen bananas (X):
60
Enter the selling price of one banana (Y):
4

outpput

Loss : Rs.12.00
'''

output
