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
