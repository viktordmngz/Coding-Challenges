'''
Create a program that simulates a shopping cart with error handling.
Your task is to:

- Create a function called handle_shopping_cart that processes customer orders
- The function should accept a list of order strings in the format "item:quantity"
- Process each order by:
  - Splitting the input string to get the item and quantity
  - Converting the quantity to an integer
  - Adding the item to a shopping cart dictionary with the quantity as value
  - If an item already exists in the cart, update its quantity

- Handle these specific errors:
  - If the input format is incorrect (missing colon), print "Invalid format: {order}"
  - If the quantity is not a valid number, print "Invalid quantity: {order}"
  - If the quantity is negative, print "Negative quantity not allowed: {order}"

- Return the completed shopping cart dictionary


INPUT
["apple:3", "banana:2", "orange:5", "grape:invalid", "apple:2", "blueberry:1", "cherry:four", "invalidorder", "cherry:-3"]

OUTPUT
Invalid quantity: "grape:invalid"
Invalid quantity: "cherry:four"
Invalid format: "invalidorder"
Negative quantity not allowed: "cherry:-3"
{'apple': 2, 'banana': 2, 'orange': 5, 'blueberry': 1}
'''

def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            if int(order.split(":")[1]) < 0:
                raise TypeError
            # Split the order and add to cart
            cart[order.split(":")[0]] = int(order.split(":")[1])
            # Handle potential errors
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")
        except TypeError:
            print(f"Negative quantity not allowed: {order}")
        except Exception as e:
            # Handle unexpected errors
            print(f"Invalid format: {order}")
    # Return the completed cart
    return cart

print(handle_shopping_cart(["apple:3", "banana:2", "orange:5", "grape:invalid", "apple:2", "blueberry:1", "cherry:four", "invalidorder", "cherry:-3"]))
