#Instructions Given:

'''
Write a program that searches for a specific string within a list of strings. The list is
initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your
task is to search for "Sam".
'''

#Simple Solution:
'''
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #initializing the list with names completes 1st task

search_name = 'Sam' #defining the name to search for completes 2nd task

if search_name in Names: #checks if input is in the list completes 3rd task
    print("Found") #if found completes 4th task
else:
    print("Not Found") #if not found completes 4th task

#result will be "Found" since "Sam" is in the list
'''

#Advanced Requirements:
#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input.


#Advanced Solution:
def search_name():
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #initializing the list with names 
    search = input("Enter a name to search for: ") #asks input from user completes 1st task and 2nd task
    if search in names: 
        print("Found")
    else:
        print("Not Found") 
        search_name() #loop

search_name()

# End of activity