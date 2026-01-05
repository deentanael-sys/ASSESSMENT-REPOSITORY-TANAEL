#Instructions Given:
#In this exercise, you'll create a simple program that asks the user a question, evaluates
#their answer, and provides feedback.

#Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Simple Solution:
question = input("What is the capital of France? ")
if question == "Paris":
    print("Correct!")
else:
    print("Incorrect.")
    
# End of activity