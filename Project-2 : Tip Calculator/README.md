# Project-2 : Tip Calculator 

## 🧠 Topics Covered
This code introduces several key Python concepts that are essential for building real-world applications:
- `print()` and `input()` functions: For user interaction.
- Data types: `float` and `int` conversions to handle numerical input.
- Arithmetic operations: Addition, division, percentage calculation.
- Variables: Used to store intermediate values and make the code readable.
- `round()` function: For formatting output to two decimal places.
- f-strings: A modern and readable way to embed variables directly into strings.

## 🚀 How This Helps in My Python Journey
This script is a great step forward from basic input/output programs. It teaches you:
- How to handle user input and convert it to the correct data type.
- How to perform calculations based on dynamic input, which is the backbone of many financial, scientific, and gaming applications.
- How to format output for clarity and professionalism, especially important in user-facing tools.
It’s practical, beginner-friendly, and sets the stage for more advanced concepts like functions, error handling, and GUIs.

## 🔄 Flow of the Code
Let’s walk through the logic step-by-step:
### 1. Welcome Message
```python
print("Welcome to the tip calculator!\n\n")
```
- Sets the tone and lets the user know what the program does.

### 2.  User Inputs
```python
bill = float(input("How much is the total bill?\n$"))
tip = int(input("How much tip would you like to give?(10, 12 or 15)\n"))
frnds = int(input("How many people will split the bill?\n"))
```
- `bill`: Total bill amount, converted to a float for decimal precision.
- `tip`: Tip percentage, converted to an integer.
- `frnds`: Number of people splitting the bill.

### 3. - Tip Calculation
```python
tip_percent = tip / 100
tip_amount = bill * tip_percent
```
- Converts the tip percentage into a decimal and calculates the tip amount.

### 4. Total Bill Calculation
```python
total_bill = bill + tip_amount
```
- Adds the tip to the original bill.

### 5. Split the Bill
```python
bill_for_each = total_bill / frnds
final_amount_pp = round(bill_for_each, 2)
```
- Divides the total bill by the number of friends.
- Rounds the result to 2 decimal places for clean currency formatting.

### 6. - Final Output
```python
print(f"\nEach person should pay - ${final_amount_pp}")
```
- Displays the final amount each person owes.

## 💡 Example Output
If the user enters:
- Bill: $120.50
- Tip: 15
- Friends: 3
The output will be:
```text
Each person should pay - $46.86
```


!

