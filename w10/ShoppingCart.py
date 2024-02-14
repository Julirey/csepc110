# File: WordleClon.py
# Author: Julio Reyes

# Summary: This program stores a list of products in a shopping cart along with their prices.
# The user has the ability to add items to the list, remove them, edit them, and see the total price of the cart.

# -Full version-

print ()
print ("     Welcome to the Shopping Cart")
print ()

shopping_cart = []
shopping_cart_prices = []
option = None

item = None
price = 0
price_total = 0
price_highest = 0

while option != "0":
    print ("----------Menu----------")
    print ("Please select an option:")
    print ("1. Add Item")
    print ("2. Remove Item")
    print ("3. Edit Item")
    print ("4. View Cart")
    print ("5. Compute Total")
    print ("0. Quit")
    option = input ("Please enter the option number: ")
    print ()

    if option == "1":
        item = input ("What item would you like to add? ")
        shopping_cart.append(item)
        price = float(input("What is the price of it? $"))
        shopping_cart_prices.append(price)
        print (f"'{item.title()}' has been added to the cart with the price of ${price:.2f}")

    elif option == "2": 
        delete_index = int(input("Which item do you want to remove? "))
        if delete_index - 1 in range(len(shopping_cart)):
            print (f"The item {delete_index}. {shopping_cart[delete_index - 1].title()} which costs ${shopping_cart_prices[delete_index - 1]:.2f} has been removed")
            shopping_cart.pop(delete_index - 1)
            shopping_cart_prices.pop(delete_index - 1)
        else :
            print ("That item number is not on the list")

    elif option == "3":
        edit_index = int(input("Which item do you want to update? "))
        if edit_index - 1 in range(len(shopping_cart)):
            shopping_cart_prices[edit_index - 1] = float(input(f'What is the new price of {shopping_cart[edit_index - 1].title()}? $'))
            print (f"The price of item {edit_index}. {shopping_cart[edit_index - 1].title()} now costs ${shopping_cart_prices[edit_index - 1]:.2f}")
        else :
            print ("That item number is not on the list")

    elif option == "4":
        print ("     Shopping Cart:")
        for i in range(1, len(shopping_cart) + 1):
            print(f"{i}. {shopping_cart[i - 1].title():<40} - ${shopping_cart_prices[i - 1]:.2f}")

    elif option == "5":
        for j in shopping_cart_prices:
            price_total += j

        print (f"Items: #{len(shopping_cart)}")
        print (f"Total: ${price_total:.2f}")

        if price_total > 0 :
            for k in range(1, len(shopping_cart_prices) + 1):
                if shopping_cart_prices[k - 1] > price_highest:
                    price_highest = shopping_cart_prices[k - 1]
                    price_highest_index = k 

            print(f"Most expensive item: {price_highest_index}. {shopping_cart[price_highest_index - 1].title()} - ${shopping_cart_prices[price_highest_index - 1]:.2f}")
            
    elif option == "0":
        print ("Thank you. Goodbye.")

    else :
        print ("That is not an available option.")
    print ()
