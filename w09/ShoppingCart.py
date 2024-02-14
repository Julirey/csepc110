# File: WordleClon.py
# Author: Julio Reyes

# Summary: This program stores a list of products in a shopping cart along with their prices.
# The user has the ability to add items to the list, remove them, and see the total price of the cart.

# -Milestone version-

print ()
print ("     Welcome to the Shopping Cart")
print ()

shopping_cart = []
option = None

while option != "0":
    print ("----------Menu----------")
    print ("Please select an option:")
    print ("1. Add Item")
    print ("2. Remove Item")
    print ("3. View Cart")
    print ("4. Compute Total")
    print ("0. Quit")
    option = input ("Please enter the option number: ")
    print ()

    if option == "1":
        add = input ("What item would you like to add? ")
        shopping_cart.append(add)
        print (f"'{add.title()}' has been added to the cart")
    elif option == "2": 
        print ("That functionality has yet to be implemented.")
    elif option == "3":
        print ("     Shopping Cart:")
        for items in shopping_cart:
            print (items.title())
    elif option == "4":
        print ("This program hasn't learned how to add numbers yet.")
    elif option == "0":
        print ("Thank you. Goodbye.")
    else :
        print ("That is not an available option.")
    print ()
