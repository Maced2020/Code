#this will be a password genterator
#started 1/22/2022
# This now generates passwords as of 1/23/2022
# This now lets you generate as many passwords as you want

import random
import sys
# this function generates a password
def password_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~;'?./"
    userchoice = input("How long would you like your password to be?: ")
    password = " "
    try:
        for i in range(int(userchoice)):
            randomletter = random.choice(alphabet)
            password = randomletter + password
        print(password)

    except:
        print("You are clearly not following the rules; you must be a hacker")
        sys.exit()


    print()
    print()
#this runs the functions and hands out a password
password_generator()

again = input("would you like another password?(y/n): ")

while again.upper() == "YES" or again.upper() == "Y":
    password_generator()
    again = input("would you like another password?(y/n): ")
else:
    print()
    print()
    print("No more passwords will be generated; Application will close")
    sys.exit()