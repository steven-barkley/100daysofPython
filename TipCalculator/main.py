print("Welcome to the tip calculator.")
total_bill =input("What was the total bill? ")
billString = list(total_bill)
cashSymbol = billString.pop(0)
total_bill = ''.join(map(str,billString)) 
print(total_bill)
people_count = input("How many people to split the bill? ")
percentage_tip = input("What percentage tip would you like toi give? 10, 12, or 15? ")
tip_calc = float(total_bill) * float(percentage_tip) / 100
solution = float(total_bill)/float(people_count) + tip_calc
print("Each person should pay: " + cashSymbol + str(solution))