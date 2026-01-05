#Instructions Given:
'''
Write a program that tests if a value is even or odd. Follow the instructions outlined
below:
'''

#Steps:
#1. The program should ask the user for a number from within the main function.
#2. The entered number should be passed to a function that determines if the value is even or odd.
#3. The function should return a message indicating whether the number is even or odd.
#4. The message returned by the function should be printed from within the main function.

#Solution:

def main(): #this is the main function
    number = int(input("Enter a number: "))  # Step 1: Ask the user for a number
    result = is_even_or_odd(number)          # Step 2: Pass the number to the function
    print(result)                            # Step 4: Print the returned message in main function

def is_even_or_odd(number): #this function checks if number inputted is even or odd
    if number % 2 == 0:
        return f"{number} is even." #step 3: Determine if even or odd and return message
    else:
        return f"{number} is odd." #step 3: Determine if even or odd and return message

main()        
# End of activity