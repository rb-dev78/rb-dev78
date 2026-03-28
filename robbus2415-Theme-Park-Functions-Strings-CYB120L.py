####################################################
## Assessment:  Theme Park Functions and Strings ##
##               CYB120L - ROBBUS2415             ##
####################################################

#####################
## Part 1: Strings ##
#####################
## Dataset ##
#############
ride_name = "Thunder Run"
park = "Coastal Adventure Park"

## 1. Predict ##
## On document

## 2. Observe ##
#print(ride_name.upper())
#print(park.split())

## 3. Analyze ##
#print(f"'{ride_name}' is a ride at {park}.")

## 4. Experiment ##
ride_name2 = "  Thunder Run  "
nospace = ride_name2.strip()
#print(f"'{nospace}' is a ride at {park}.")
#print(f"'{ride_name2}' is a ride at {park}")

## 5. Challenge Thinking ##
#name_light = ride_name.replace("Thunder", "Lightning")
#print(name_light)

## 6. Extend ##
#desc = "It's a thrill coaster!"
#print(len(desc))
#print("thrill" in desc)

#######################
## Part. 2 Functions ##
#######################

## 1. Predict ##
## On document

## 2. Observe ##
#def greet_guest(name):
#    return f"Welcome to {park}, {name}!"
#print(greet_guest("Ava"))

## 3. Analyze ##
#def format_ride_info(ride, park):
#    return f"Ride: {ride} - Park: {park}"
#print(format_ride_info("Thunder Run", "Coastal Adventure Park"))

## 4. Experiment ##
#def format_ride_info(ride, park, price):
#    return f"Ride: {ride} - Park: {park} - Price: ${price}"
#print(format_ride_info("Thunder Run", "Coastal Adventure Park", 10.99))

## 5. Challenge Thinking ##
#def discount_price(price, discount_percent):
#    return price - (price * discount_percent / 100)
#print(discount_price(10.99, 20))

## 6. Extend ##
def greet_guest(name):
    return f"Welcome to {park}, {name}!"
def format_ride_info(ride, park):
    return f"Ride: {ride} - Park: {park}"
def generate_ticket_receipt(customer_name, ride_name, price):
    print(greet_guest(customer_name))
    print(format_ride_info(ride_name, park))
    print(f"Price: ${price}")
    print("Thank you for your visit!")
generate_ticket_receipt("Ava", "Thunder Run", 10.99)

      

