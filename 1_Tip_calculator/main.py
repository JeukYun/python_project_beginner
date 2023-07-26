print("Welcome to tip calculator")

total_bill = float(input("What was the total bill? $"))

tip = float(input("How much tip would you like to give 10, 12, or 15??"))

each_people = int(input("How many people to split the bill?"))


total = round((total_bill+(total_bill/100)*tip)/each_people,2)
total = "{:.2f}".format(total)
print(f"Each person should pay:{total}")