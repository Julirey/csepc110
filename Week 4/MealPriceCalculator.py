# File: MealPriceCalculator.py
# Author: Julio Reyes

# Documentation: This program asks for the user to input a series of values that represent the 
# prices of a meal menu in addition to other relevant information, then it will output the total
# price as well as subtotal, sales tax, and change (if any).

# -Full version-

print ("\n     Welcome to Meal Price Calculator")
print ()

child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
discount_elegibility = (input("Are you elegible for Valentine's couple discount? [YES/NO] "))

if discount_elegibility.lower() == "yes":
    discount = 25
else :
    discount = 0
 
child_subtotal = child_meal_price * child_number
adult_subtotal = adult_meal_price * adult_number

all_subtotal = child_subtotal + adult_subtotal

# This allows it to apply the discount before the taxes 
discount_total = (all_subtotal * discount) / 100
all_subtotal_discounted = all_subtotal - discount_total

tax_rate_total = (all_subtotal_discounted * tax_rate) / 100 
all_total = (all_subtotal_discounted + tax_rate_total) - discount_total

print ()
print (f"{'Subtotal:':<25} ${all_subtotal:.2f}")
if discount_elegibility.lower() == "yes":
    print (f"{'Discount:':<25} ${discount_total:.2f}")
    print (f"{'Subtotal w/ Discount:':<25} ${all_subtotal_discounted:.2f}")
print (f"{'Sales Tax:':<25} ${tax_rate_total:.2f}")
print (f"{'Total:':<25} ${all_total:.2f}")
print ()

payment = float(input("What is the payment amount? $"))
print ()

change = payment - all_total

# This allows it to display the missing amount later without it being a negative number
change_missing = all_total - payment 

# Checks whether the payment amount is enough, if YES - displays the change, 
# if NOT - displays missing amount, if PERFECT - congratulates user
if payment >= all_total: 
    if change == 0 :
        print ("Congratulations! Your payment amount was perfect!")
    else :
        print (f"{'Change:':<25} ${change:.2f}")
else : 
    print (f"You are ${change_missing:.2f} short to afford it.")

print ()