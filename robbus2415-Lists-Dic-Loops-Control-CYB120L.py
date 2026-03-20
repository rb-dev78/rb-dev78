#########################################################################
## Assessment: Python for Lists, Dictionaries, Loops, and Control Flow ##
##                          ROBBUS2415 - CYB120L                       ##
#########################################################################

####################
## Part 1: Lists  ##
####################
## Dataset ##
menu_items = ["coffee", "tea", "sandwich","cake"]
prices = [2.50,2.00,5.00,3.50]

## Predict ##
## On document
#print(menu_items[1])
#print(prices[-1])

## Observe
## On document

## Analyze ##
#for i in range(len(menu_items)):
#    print(menu_items[i],'-', prices[i])

## Experiment ##
#menu_items.append("smootie")
#prices.append(4.00)
#for i in range(len(menu_items)):
#    print(menu_items[i],'-', prices[i])

## Challenge Thinking (zip) ##
#for item, price in zip(menu_items, prices):
#    print(item, "-", price)

## Extend ##
#under_3 = []
#for item, price in zip(menu_items, prices):
#    if price < 3:
#        under_3.append(item)
#    print(under_3)

##########################
## Part 2. Dictionaries ##
##########################
## Dataset ##
menu_dict={
    "coffee":2.50,
    "tea":2.00,
    "sandwich":5.00,
    "cake":3.50
    }

## Predict ##
# On document

## Observe
## On document
#print(menu_dict['tea'])

## Analyze ##
#for item, price in menu_dict.items():
#    print("Menu Items:", item, "- Price: $", format(price, ".2f"))

## Experiment ##

#menu_dict["smootie"] = 4.00
#for item, price in menu_dict.items():
#          print(item, "-", price)

## Challenge Thinking ( 10%) ##
#for item in menu_dict:
#    menu_dict[item] = round(menu_dict[item] * 1.10, 2)
#print(menu_dict)

## Extend (20%) ##

#discounted_menu = {}
#for item, price in menu_dict.items():
#    discounted_menu[item] = price * 0.80
#print(discounted_menu)

##################################
## Part 3. Loops + Control Flow ##
##################################
## Dataset ##
orders =["coffee","cake","coffee","sandwich","tea","coffee"]

## Predict ##
## On document

## observe ##
#for order in orders:
#         if order == 'coffee':
#            print('Coffee order found!')

## Analyze ##

#count = 0
#for order in orders:
#    if order == "coffee":
#        count += 1
#print(count)

## Experiment ##

#total = 0
#for order in orders:
#   total += menu_dict[order]
#print(total)

## Challenge Thinking ##

#total = 0
#for order in orders:
#    total += menu_dict[order]
#if total > 15:
#    print("Warning: Total exceeds $15")
#print(total)

## Extend ##

total = 0
for order in orders:
    price = menu_dict[order]
    print(order, "-", "$" + format(price, ".2f"))
    total +=  price
print("Total:", "$" + format(total, ".2f"))
          




































