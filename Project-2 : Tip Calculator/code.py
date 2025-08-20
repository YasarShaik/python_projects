print("Welcome to the tip calculator!\n\n")

# Input and type declerations
bill = float(input("How much is the total bill?\n$"))
tip = int(input("How much tip would you like to give?(10, 12 or 15)\n"))
frnds = int(input("How many people will split the bill?\n"))

# Calculation Processes
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_for_each = total_bill / frnds
final_amount_pp = round(bill_for_each, 2)

# Output.
print(f"\nEach person should pay - ${final_amount_pp}")
