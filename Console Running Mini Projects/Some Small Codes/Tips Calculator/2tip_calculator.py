print("Welcome to the tip calculator.")
amount=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_amount=amount*12/100
a=amount+tip_amount
split=int(input("How many people to split the bill?"))
a2=a/split
final=f"{a2:.2f}" # This line returns the floating point of 2 digits after the decimal point
print(f"Each person should pay: ${final}")