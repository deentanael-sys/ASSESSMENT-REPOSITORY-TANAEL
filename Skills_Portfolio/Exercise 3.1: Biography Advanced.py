#Instructions Given:
#In this exercise, you'll create a program that stores and prints your name, hometown,
#and age to the console using a Python dictionary.

#Steps:
# 1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
# 2. Print the values on separate lines using a single print() statement.
# 3. Use variables with appropriate data types for each piece of information.

#Simple Solution:

'''
dictionary = {
    "name": "Deen Tanael",
    "hometown": "Catanduanes",
    "age": 22
}

print(dictionary["name"] + "\n" + dictionary["hometown"] + "\n" + str(dictionary["age"]))
'''

#Advanced Requirements:
#1. Have the user input their name, hometown, and age instead of hardcoding the values.
#2. Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python? 
#3. Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

#Advanced Solution:

#1. input from user solves 1st task, and by assigning input to variables it also solves 2nd task
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

#checks if age is an integer and loops until valid input is given completes 3rd task
age = input("Enter your age: ")
while not age.isdigit():
    print("Please enter a valid number for age.")
    age = input("Enter your age: ")
age = int(age)


dictionary = {

    "name": name,
    "hometown": hometown,
    "age": age
}

#printing the values just to check :P
print(dictionary["name"] + "\n" + dictionary["hometown"] + "\n" + str(dictionary["age"]))

# End of activity