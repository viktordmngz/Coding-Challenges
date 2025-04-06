'''
Goods & Construction

Create a function named whatToBuy that receives four arguments:

* First argument is a list of numbers that indicate the price of a construction item
* Second argument is a list of numbers that indicates the quantity of each construction item
* Third argument is a number indicating the total price allowed for each item
* Fourth argument is a list of construction names

The function calculates, for each item, the total price required to buy it.
The total price for each item is calculated like this:

(quantity * price) / (average_quantity * average_price)

* Remember that the average can be found like so: average = sum(lst)/len(lst)


The function will return a list of two elements:
* The first element is a SORTED list of all the construction names whose total price is smaller than the restriction (third argument).
* The second element is a number, which indicates how many construction items were removed.

'''

def whatToBuy(prices, quantities, restriction, names):
  # Write code here
  items = []
  final = []
  for i in range(len(prices)):
    total = (quantities[i]*prices[i])/((sum(quantities)/len(quantities))*(sum(prices)/len(quantities)))
    if total < restriction:
      items.append(names[i])
  items.sort()
  final.append(items)
  final.append(len(names)-len(items))
  return final
