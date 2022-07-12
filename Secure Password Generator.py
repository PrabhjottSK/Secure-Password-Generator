# Prabhjott Singh Kusrath
# This program is a password generator aimed to provide a more secure encryption.

import random

uppercase = "abcdefghijklmnopqrstuvwxyz" # The uppercase characters to be used in the password.
lowercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # The lowecase characters to be used in the password.
special = "!@#$%^&*()-+`~" # The special characeters to be used in the password.
char_list = uppercase + lowercase + special # Creates a list conbining all varieties of characters.

digits = int(input("Enter the amount of digits you'd like your password to be: ")) # Asks for the user to input the length of the password.
pass_amount = int(input("Enter the amount of passwords you'd like: ")) # Asks the user how many passwords they desire.

for i in range(0, pass_amount): # Runs the password randomizer based on how many passwords the user inputted. 
    pw = "" # Initializes the variable
    for i in range(0, digits): # Runs the randomizer for each character based on how my digits the user inputted.
        random_char = random.choice(char_list)
        pw = pw + random_char
    print("Here's your", digits, "digit password:" , pw)
