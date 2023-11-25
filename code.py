print("Welcome to the tip calculator")
print("We will help you to solve the tip problem")
total_bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
total_tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + total_tip
bill_per_person = total_bill_with_tip / people
print(f"Each person should pay: ${bill_per_person:.2f}")
print("Hope you enjoy using this tip calculator")
