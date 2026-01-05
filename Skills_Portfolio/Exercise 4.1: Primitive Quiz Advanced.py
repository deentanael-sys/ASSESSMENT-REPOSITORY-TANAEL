#Instructions Given:
#In this exercise, you'll create a simple program that asks the user a question, evaluates
#their answer, and provides feedback.

#Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Simple Solution:
'''
question = input("What is the capital of France? ")
if question == "Paris":
    print("Correct!")
else:
    print("Incorrect.")
''' 
#Advanced Requirements:
#1. Ignore Capitalization: Modify your program to accept answers regardless of these
#capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
#2. Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. 
#3. Provide feedback for each question.

#Advanced Solution:
print("Welcome to the European Capitals Quiz!")
score = 0

#10 questions stored in a dictionary Solves Task 2
questions = {
    "What is the capital of France? ": "paris",
    "What is the capital of United Kingdom? ": "london",
    "What is the capital of Italy? ": "rome",
    "What is the capital of Spain? ": "madrid",
    "What is the capital of Germany? ": "berlin",
    "What is the capital of Netherlands? ": "amsterdam",
    "What is the capital of Belgium? ": "brussels",
    "What is the capital of Austria? ": "vienna",
    "What is the capital of Switzerland? ": "bern",
    "What is the capital of Greece? ": "athens"
}
#I dont even know half of these capitals lol

#this block of code takes each question from the dictionary, as "question", and its corresponding answer as "correct_answer"
#then asks the user the question and checks if the answer is correct while ignoring capitalization which solves the 1st task

for question, correct_answer in questions.items(): #looping through dictionary items
    user_answer = input(question).lower() #ignores capitalization
    if user_answer == correct_answer:#checking answer
        print("Correct!")
        score += 1 #increments score for every correct answer
    else:
        print(f"Incorrect. The answer was {correct_answer.capitalize()}.") #Provides feedback by giving correct answer
                                                                           #Solves Task 3


print(f"Your total score is {score} out of {len(questions)}.") #yeah just gives total score :)


# End of activity