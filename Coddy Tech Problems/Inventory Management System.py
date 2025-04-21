'''
Inventory Management System

1) Create a function named add_item that takes three arguments: item (string), price (float), and stock (int). The function should:

- Check if the item already exists in the inventory dictionary.
    - If it does, print "Error: Item '<item>' already exists.".
- If the item does not exist, add it to the inventory with the provided price and stock.
    - Store the price as a float and the stock as an integer.
- Print "Item '<item>' added successfully.".


2) Create a function named update_stock that takes two arguments: item (string) and quantity (int). The function should:

- Check if the item exists in the inventory dictionary.
    - If it does not exist, print "Error: Item '<item>' not found.".
- If the item exists, calculate the new stock by adding the quantity to the current stock.
    - If the new stock is negative, print "Error: Insufficient stock for '<item>'." and do not update.
    - Otherwise, update the stock in the inventory.
- Print "Stock for '<item>' updated successfully.".


3) Create a function named check_availability that takes one argument: item (string). The function should:

- Check if the item exists in the inventory dictionary.
    - If it does not exist, return "Item not found".
- If the item exists, return the current stock of the item.
'''
inventory = {}

def add_item(item,price,stock):
    if item in inventory:
        print(f"Error: Item \'{item}\' already exists.")
    else:
        inventory.update({item: {'price': price, 'stock': stock}})
        print(f"Item \'{item}\' added successfully.")


def update_stock(item,quantity):
    if item not in inventory:
        print(f"Error: Item \'{item}\' not found.")
    else:
        try:
            inventory[item]['stock'] += quantity
            if inventory[item]['stock'] < 0:
                inventory[item]['stock'] -= quantity
                raise ValueError
        except ValueError:
            print(f"Error: Insufficient stock for \'{item}\'.")
        else:
            print(f"Stock for \'{item}\' updated successfully.")


def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]['stock']

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
