print("Welcome to the tip calculator.")
total_bill =input("What was the total bill?")
people_count = input("How many people to split the bill?")
percentage_tip = input("What percentage tip would you like toi give? 10, 12, or 15?")
print("Each person should pay: %.2f" % (int(percentage_tip)*int(total_bill)/int(people_count)))