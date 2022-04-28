#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_before_tip = input("What was the total bill? ")
tip_percent = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people would like to split the bill? ")
tip = int(bill_before_tip) * (int(tip_percent) / 100)
total_bill = tip + int(bill_before_tip)
split_bill = round(total_bill / int(people), 2)
final_amount = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_amount}")