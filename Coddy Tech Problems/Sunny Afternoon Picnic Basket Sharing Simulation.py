'''
Create a function named share_picnic_basket that receives friends, basket, and rounds as its parameters.

The function simulates sharing a picnic basket among friends on a sunny afternoon, distributing items fairly over multiple rounds.

Parameters:
* friends (list of str): A list of strings representing the names of friends attending the picnic.
* basket (dict): A dictionary representing the picnic basket, where keys are item names (str) and values are the quantities of each item (int).
* rounds (int): An integer representing the number of rounds of sharing.

The function should simulate the process of sharing the picnic items among friends over multiple rounds, following these rules:
* In each round, friends take turns choosing items from the basket.
* The order of friends remains the same as in the input list for each round.
* Each friend can take only one item per turn, but they can choose which item to take.
* Friends always try to take their favorite item first, which is the first letter of their name (e.g., "Alice" prefers items starting with "A").
* If their favorite item is not available, they take the next available item alphabetically.
* If a friend cannot take any item in a round, they skip their turn.
* The sharing continues until all rounds are completed or the basket is empty.

The function returns a dictionary where keys are friend names and values are lists of items they received during the picnic.


Constraints:
1 ≤ len(friends) ≤ 10
1 ≤ len(basket) ≤ 20
1 ≤ rounds ≤ 100
All friend names and item names are lowercase alphabetic strings.
All item quantities in the basket are positive integers.


This challenge requires expert use of loops to iterate through rounds, friends, and items, as well as complex conditional statements to handle item selection and availability.
You may need to use nested loops and loop control statements to implement the logic efficiently.
'''

def share_picnic_basket(friends, basket, rounds):
  final = {}
    for item in friends:
      final[item] = []
    # while loop?
    while rounds > 0 and sum(basket.values()) > 0:
      #print(f"\nROUND: {rounds}")
      for name in final:
        available_items = [x for x in basket if basket[x] != 0]
        if available_items == []:
          return final
        available_items.sort()
        available_items_letters = [x[0] for x in available_items]
        #print(f"AVAILABLE ITEMS: {available_items}")
        if name[0] in available_items_letters:
          food_index = available_items_letters.index(name[0])
        else:
          food_index = 0
        final[name].append(available_items[food_index])
        basket[available_items[food_index]] -= 1
        #print(f"NAME: {name}\tCHOICE: {available_items[food_index]}\tBASKET: {basket}")
      rounds -= 1
  return final

test1 = {'friends':['alice','bob'],'basket':{'banana':1,'apple':2}, 'rounds':1}
test2 = {'friends':['alice','bob','charlie'],'basket':{'banana':2,'apple':3,'cookie':1},'rounds':2}
test3 = {'friends':['dave','eve'],'basket':{"fig":1,"egg":2,"donut":1},'rounds':3}
test4 = {'friends':['frank','george','harry'],'basket':{"grape":2,"fig":3,"honey":1},'rounds':2}
test5 = {'friends':['kate','leo','mike'],'basket':{"kiwi":1,"lemon":2,"mango":3},'rounds':3}
test6 = {'friends':['mike','nina','olivia','paul'],'basket':{"noodles":3,"orange":2,"pizza":5,"muffin":4},'rounds':6}
test7 = {'friends':['adam','bella','chris','diana','ethan'],'basket':{"banana":1,"cherry":1,"elderberry":1,"apple":1,"date":1},'rounds':2}
test8 = {'friends':['finn'],'basket':{"fries":10},'rounds':10}

print(test1['friends'],test1['basket'],test1['rounds']) # OUTPUT: {'alice': ['apple'], 'bob': ['banana']}
print(test2['friends'],test2['basket'],test2['rounds']) # OUTPUT: {'alice': ['apple', 'apple'], 'bob': ['banana', 'banana'], 'charlie': ['cookie', 'apple']}
print(test3['friends'],test3['basket'],test3['rounds']) # OUTPUT: {'dave': ['donut', 'egg'], 'eve': ['egg', 'fig']}
print(test4['friends'],test4['basket'],test4['rounds']) # OUTPUT: {'frank': ['fig', 'fig'], 'george': ['grape', 'grape'], 'harry': ['honey', 'fig']}
print(test5['friends'],test5['basket'],test5['rounds']) # OUTPUT: {'kate': ['kiwi', 'lemon'], 'leo': ['lemon', 'mango'], 'mike': ['mango', 'mango']}
print(test6['friends'],test6['basket'],test6['rounds']) # OUTPUT: {'mike': ['muffin', 'muffin', 'muffin', 'pizza'], 'nina': ['noodles', 'noodles', 'noodles', 'pizza'], 'olivia': ['orange', 'orange', 'muffin'], 'paul': ['pizza', 'pizza', 'pizza']}
print(test7['friends'],test7['basket'],test7['rounds']) # OUTPUT: {'adam': ['apple'], 'bella': ['banana'], 'chris': ['cherry'], 'diana': ['date'], 'ethan': ['elderberry']}
print(test8['friends'],test8['basket'],test8['rounds']) # OUTPUT: {'finn': ['fries', 'fries', 'fries', 'fries', 'fries', 'fries', 'fries', 'fries', 'fries', 'fries']}
