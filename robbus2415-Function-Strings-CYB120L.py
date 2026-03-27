#################################################
## Assessment: Python for Function and Strings ##
##              CYB120L - ROBBUS2415           ##
#################################################

#####################
## Part 1. Strings ##
#####################
## Dataset ##
#############
book_title = "The Great Gatsby"
author = "F. Scott Fitzgerald"


## 1. Predict ##
## On document

## 2. Observe ##
#print(book_title.upper())
#print(author.split())

## 3. Analyze ##
#print(f"'{book_title}' is written by {author}.")

## 4. Experiment ##
#book_title2 = " The Great Gatsby "
#print(book_title2.strip())

## 5. Challenge Thinking ##
#print(book_title.replace("Gatsby", "Adventure"))

## 6. Extend ##
## The description came from the google by the book. 
desc = "A classic American novel set in 1922 Long Island, exploring the Jazz Age's hedonism, disillusionment, and moral decay."
#print(len(desc))
#print("classic" in desc)

#######################
## Part 2. Functions ##
#######################

## 1. Predict ##
## On document

## 2. Observe ##
#def greet_customer(name):
#    return f"Welcome, {name}!"
#print(greet_customer("Alice"))

## 3. Analyze ##
#def format_book_info(title, author):
#    return f"Title: {title} - Author: {author}"
#print(format_book_info("The Great Gatsby", "F. Scott Fitzgerald"))

## 4. Experiment ##
#def format_book_info_w_price(title, author, price):
#    return f"Title: {title} - Author: {author} - Price: {price}"
#print(format_book_info_w_price("The Great Gatsby", "F. Scott Fitzgerald", 29.95))

## 5. Challenge Thinking ##
#def discount_price(price,discount_percent):
#    return price - (price * discount_percent / 100)
#print(discount_price(29.95, 10))

## 6. Extend ##
def greet_customer(name):
    print(f"Welcome, {name}!")
def format_book_info(title):
    return f"Title: {title} - Author: F. Scott Fitzerald"
def generate_receipt(customer_name, book_title, price):
    greet_customer(customer_name)
    print(format_book_info(book_title))
    print(f"Price: ${price}")
    print("Thank you for your purchase!")
generate_receipt("Alice", "The Great Gatsby", "10.99")

