##########################################
## Assessment: Python for Login Systems ##
##        ROBBUS2415 - CYB120L          ##
##########################################

user_credentials = {
   "rob":"shin3",
    "juju":"l337",
    "kat":"l@@k!"
    }
#################
## Part 1 to 3 ##
#################

#def login():
#    attempts = 0

#    while attempts < 3:
#        usern = input("Enter username: ")
#        passw = input("Enter password: ")

#        if usern in user_credentials:
#            if user_credentials[usern] == passw:
#                print("Access granted")
#                return
#            else:
#                print("Wrong Username or Password")
#        else:
#            print("Access denied")
#        attempts += 1
#        
#    print("Account locked")
#
#login()

#############
## Part 4. ##
#############

#def register_user():
#    usern = input("Enter new username: ")
#
#    if usern in user_credentials:
#        print("Username already taken ")
#    else:
#        passw = input("Enter new password: ")
#        user_credentials[usern] = passw
#       print(" User registered")
        
#register_user()

#############
## Part. 5 ##
#############

login_history = {
    "rob": [],
    "juju": [],
    "kat": []
    }
def login():
    usern = input("Enter username: ")
    passw = input("Enter password: ")

    if usern in user_credentials:
        if user_credentials[usern] == passw:
            print("Access granted")

            ip = input("Enter IP address: ")
            login_history[usern].append(ip)

            print("Login History:", login_history[usern])
        else:
            print("Access denied")
    else:
        print("Access granted")

login()

