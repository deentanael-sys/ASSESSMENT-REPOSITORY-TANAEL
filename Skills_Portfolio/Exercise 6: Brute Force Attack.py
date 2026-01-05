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

correct_password = "12345" #the password (duh)
 
while True: #since its brute force this is a loop that will continue running until password is correct
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Password accepted.")
        break #this breaks the loop when password is correct
    else:
        print("Incorrect password. Please try again.")
        #since there's no break here it loops again

# End of activity