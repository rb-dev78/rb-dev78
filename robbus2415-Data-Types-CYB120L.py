############################
## Assessment: Data Types ##
##  ROBBUS2415 - CYB120L  ##
############################

#####################################
# Part 1 - Data Types and Operators #
#####################################

## 1. Predict

#print(3+2)

## 2. Observe

#morning_failed = 3
#evening_failed = 2
#total_failed = morning_failed + evening_failed
#print(total_failed)

## 3. Analyze

#type(morning_failed)
#type(str(morning_failed) + str(evening_failed))
#"3" + "2"  #compare to 3 + 2

## rewrite ##
#morning_failed = 3  #added
#evening_failed = 2  # added 
#print(type(morning_failed))
#print(type(str(morning_failed) + str(evening_failed)))
#print("3" + "2" )
#print(3+2)
## successful ##

## 4. Experiment

#morning_failed = 3
#evening_failed = 2.5
#total_failed = morning_failed + evening_failed
#print(total_failed, type(total_failed))


## 6. Extend
#morning_failed = 3
#evening_failed = 2
#total_failed = morning_failed + evening_failed
#print(f"LOGGING LOG: Morning: {morning_failed} | Evening: {evening_failed} | Total: {total_failed} ")

######################################
# Part 2 - Boolean Logic and If/Else #
######################################

## 1. Predict
## On document

## 2. Observe 
#total_failed = 7 #3
#if total_failed > 5:
#    print("Access locked")
#else:
#    print("Access permitted")

## 3. Analyze
## On document

## 4. Experiment
#failed_logins = 5 #added for expereiment
#if failed_logins > 5:
#    print("account locked")
#elif failed_logins == 5:
#    print("Warning: near lockout")
#else:
#    print("Access permitted")

## 5. Challenge Thinking
## On document

## 6. Extend
#morning_failed = 3
#evening_failed = 0.5 # 2, 2.5
#total_failed = morning_failed + evening_failed
#if total_failed > 5:
#    print("Account locked")
#elif total_failed == 5:
#    print("Warning: near lockout")
#else:
#    print("Access permitted")

#######################
# Part 3 - Error Type #
#######################

## 1. Predict
## On document
#print("Login time is: " + 10)

## 2. Observe

#print("Login time is:" + 10)

## 3. Analyze

#print("Login time is: " + str(10)) ## added str
#print("Login time is: ", 10) # without + and str

## 4. Experiment

#print("Number is: " + 6.2)
#print("Number is: " + str(6.2))

## 5. Challenge Thinking
## On document

## 6. Extend

def login_summary(user, count):
    return f"User {user} has {int(count)} failed attempts."
print(login_summary("ada", "3"))

    








