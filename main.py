print("Welcome to the tip calculator.")
amount = input("What was the amount of total bill ?\t")
percent_tip = input("What percentage tip would you like to give? 10, 12 or 15?\t")
people_split = input("How many people to split the bill?\t")

each_pay_bill = (int(amount) + int(amount)*(float(percent_tip)/100) / int(people_split))

print("Each person should pay:",round(each_pay_bill))
