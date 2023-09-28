# File: MealPriceCalculator.py
# Author: Julio Reyes

# Documentation: This program asks for the user to input a series of values that represent the 
# prices of a meal menu in addition to other relevant information, then it will output the total
# price as well as subtotal, sales tax, and change (if any).

# -Milestone requirements version-

print ("\n     Welcome to Meal Price Calculator")
print ()

child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

child_subtotal = child_meal_price * child_number
adult_subtotal = adult_meal_price * adult_number

all_subtotal = child_subtotal + adult_subtotal

print (f"\nSubtotal: ${all_subtotal}")
print ()


