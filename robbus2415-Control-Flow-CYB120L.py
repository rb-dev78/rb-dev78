##############################
## Assessment: Control Flow ##
##############################

####################
## Part 1. Lisits ##
####################
## Dataset: ##
##############
#parts = ["headlight", "brake pads", "starter", "alternator", "tire", "windshield wipers"]
#prices = [79.99,49.99,149.99,199.99,99.99,24.99]

## 1. Predict ##
## On document

## 2. Observe ##
#print(parts[1])
#print(prices[-1])

## 3. Analyze ##
#for i in range(len(parts)):
#    print(parts[i], "-", prices[i])

## 4. Experiment ##

#parts.append("spark plugs")
#prices.append(14.99)
#for i in range(len(parts)):
#    print(parts[i], "-", prices[i])

## 5. Challenge Thinking ##
#for part, price in zip(parts, prices):
#    print(part, "-", price)

## 6. Extend ##
#under_100 = [part for part, price in zip(parts, prices) if price < 100]
#print(under_100)

#########################
## Part 2. Dictonaries ##
#########################
## Dataset ##
#############
parts_dict={
    "headlight":79.99,
    "brake pads":49.99,
    "starter":149.99,
    "alternator":199.99,
    "tire":99.99,
    "windshield wipers":24.99
    }

## 1. Predict ##
## On Document

## 2. Observe ##
#print(parts_dict["brake pads"])

## 3. Analyze ##
#for part, price in parts_dict.items():
#    print(f"Part: {part} - Price: ${price:.2f}")

## 4. Experiment ##
#parts_dict["spark plugs"]=14.99
#for part, price in parts_dict.items():
#    print(part, price)

## 5. Challenge Thinking ##
#for part in parts_dict:
#    parts_dict[part] = round(parts_dict[part] * 1.10, 2)
#    print(parts_dict)

## 6. Extend ##
#discounted_parts = {}
#for part, price in parts_dict.items():
#    discounted_parts[part]= round(price * 0.80, 2)
#print(discounted_parts)

##################################
## Part 3. Loops + Control Flow ##
##################################
## Dataset ##
#############
orders = ["headlight", "tire", "brake pads", "starter", "alternator", "windshield wipers"]

## 1. Predict ##
## On document

## 2. Observe ##
#for order in orders:
#    if order == "headlight":
#        print("Headlight order found!")

## 3. Analyze ##
#count = 0
#for order in orders:
#    if order == "headlight":
#        count += 1
#print(count)

## 4. Experiment ##
#total = 0
#for order in orders:
#    total += parts_dict[order]
#print(total)

## 5. Chakllenge Thinking ##
#if total > 300:
#    print("Warning: total execceds $300")

## 6. Extend ##
total = 0
for order in orders:
    price = parts_dict[order]
    total += price
    print(order, "-", price)
print("Total:", total)



























