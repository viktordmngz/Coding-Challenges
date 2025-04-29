'''
This was part of a recap lesson, which had 4 separate challenges.
I have merged them together into one code.
I will leave comments on what each function is supposed to do and how the parameters should be formatted.
'''

inventory = {}

# Adding items to the inventory dictionary
def add_item(item,price,stock):
    # Check if the item already exists
    if item in inventory:
        print(f"Error: Item \'{item}\' already exists.")
    else:
        # inventory will be a dictionary holding a dictionary
        inventory.update({item: {'price': price, 'stock': stock}})
        print(f"Item \'{item}\' added successfully.")


# Update the quantity of a specific item
def update_stock(item,quantity):
    # Make sure the item is in the dictionary
    if item not in inventory:
        print(f"Error: Item \'{item}\' not found.")
    else:
        try:
            # NOTE: Probably a better way to do this, but I found this works
            '''  --ALTERNATE (and better) SOLUTION--
                 --CAN REMOVE THE TRY-EXCEPT BLOCK TOO--
            if inventory[item]['stock'] + quantity > 0:
                inventory[item]['stock'] += quantity
                print(f"Stock for '{item}' updated successfully.")
            else:
                print(f"Error: Insufficient stock for '{item}'.")
                --ERASE/COMMENT OUT REST OF CODE BELOW THIS LINE--
            '''
            inventory[item]['stock'] += quantity
            # Make sure the stock does not go negative
            if inventory[item]['stock'] < 0:
                inventory[item]['stock'] -= quantity
                raise ValueError
        except ValueError:
            print(f"Error: Insufficient stock for \'{item}\'.")
        else:
            print(f"Stock for \'{item}\' updated successfully.")


# Checks the stock of the item in the inventory
def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]['stock']

# Generates a revenue for all the items sold in the sales dictionary
# 'sales' is a dictionary with item names and the the quantity each item sells
def sales_report(sales):
    total = 0
    # .items() method returns key-value pairs for each item in sales dictionary
    for item,quantity in sales.items():
        # ERROR CHECKS - Same as previous functions
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        # Check to make sure inventory has enough stock of that item
        if inventory[item]["stock"] < quantity:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        inventory[item]["stock"] -= quantity
        total += quantity*inventory[item]["price"]
    return f"Total revenue: ${total:.2f}"
