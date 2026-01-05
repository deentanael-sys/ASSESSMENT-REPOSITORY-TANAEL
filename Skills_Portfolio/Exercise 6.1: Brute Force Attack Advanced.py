#Instructions Given:
'''
Write a program that simulates a password entry system. The correct password is
defined as 12345. The program should keep asking the user to enter the password until
they provide the correct one.
'''

#Steps:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.

#Simple Solution:
'''
correct_password = "12345" #the password (duh)
 
while True: #since its brute force this is a loop that will continue running until password is correct
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Password accepted.")
        break #this breaks the loop when password is correct
    else:
        print("Incorrect password. Please try again.")
        #since there's no break here it loops again
'''

#Advanced Requirement:
# Modify the program to include a maximum of 5 password attempts.
# If the user enters the wrong password, inform them of the remaining attempts.
# If the maximum number of attempts is reached, inform the user that the authorities have been alerted.

#Advanced Solution:
correct_password = "12345" #corect password
max = 5 #maximum attempts
attempts = 0 #defining attempts variable (will change later)

while attempts < max: # so this loop is different because it will only run while attempts are less than the max variable(5)
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Password accepted.")
        break #still breaks the loop if password is correct
    else:
        attempts += 1 #increments attempts by 1 each time password is wrong
        remaining_attempts = max - attempts #this variable calculates remaining attempts to be shown to user
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left. Please try again.") #shows remaining attempts
        else:
            print("Maximum attempts reached. Authorities have been alerted.") #corny but ok


# End of activity