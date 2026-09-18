import os
# Imports the os module used to clear the CMD screen


products = ['Cheese', 'Milk', 'Bread', 'Water', 'Coffee', 'Ham', 'Bacon']
prices = [95, 28, 22, 13, 55, 36, 42]


def clear_screen():
    os.system('cls')
# Clears the CMD screen before starting the POS system


def display_products():
    for i in range(0, len(products)):
        print(str(i + 1) + '. ' + products[i] + ' R' + format(prices[i], '.2f'))
# Displays all available products and their prices


def add_items():
    selected_items = []
    selected_prices = []
    sentinel = True
    for item in range(0, 20):
        try:
            selection = int(input('Select an item: '))
        except ValueError:# Lines 28- 30 makes the system immune to letters outside of the intended range
            print('Invalid input. Please enter a number from 1 to 8.')
            continue
        if selection < 1 or selection > 8:# Lines 31-33 makes the system immune to numbers outside of the intended range
            print('Invalid selection. Please select a number from 1 to 8.')
            continue
        if selection == 8:# Selecting 8 ends the item selection process
            sentinel = False
        if sentinel == False:# The sentinel variable controls when the loop exits
            break
        selected_items.append(products[selection - 1])# lines 32 and 33 the selected product and its price to their respective lists
        selected_prices.append(prices[selection - 1])
    return selected_items, selected_prices
# Allows the user to select multiple products


def calculate_total(selected_prices):
    total = 0
    for price in selected_prices:
        total += price
    return total
# Calculates the total price of all items


def display_receipt(selected_items, selected_prices, total):
    print('\n')
    for item in range(0, len(selected_items)):
        print(selected_items[item] + ' R' + format(selected_prices[item], '.2f'))
    print('--------------------')
    print('Total: R' + format(total, '.2f'))
# Displays the customer's selected products, prices and total


def main():
    clear_screen()# Clears the CMD screen before starting
    print('Welcome to POS\n\nAvailable products:\n')  # lines 52 and 53 displays the welcome message and available products
    display_products()
    print('8. Done\n\n')
    selected_items, selected_prices = add_items()# Allows the user to select their items
    total = calculate_total(selected_prices)# calculates the total
    display_receipt(selected_items, selected_prices, total)# Displays the final receipt
    input('\nPress Enter to exit...')
# Runs the entire POS system


main()
# Starts the POS system