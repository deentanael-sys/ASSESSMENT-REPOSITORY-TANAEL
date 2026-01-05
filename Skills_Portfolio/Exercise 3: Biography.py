#Instructions Given:
#In this exercise, you'll create a program that stores and prints your name, hometown,
#and age to the console using a Python dictionary.

#Steps:
# 1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
# 2. Print the values on separate lines using a single print() statement.
# 3. Use variables with appropriate data types for each piece of information.

#Simple Solution:
dictionary = {
    "name": "Deen Tanael",
    "hometown": "Catanduanes", #this is in the Philippines :DD
    "age": 22
}

print(dictionary["name"] + "\n" + dictionary["hometown"] + "\n" + str(dictionary["age"]))

# End of activity