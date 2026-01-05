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
#1. Ignore Capitalization: Modify your program to accept answers regardless of the
#capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
#2. Multiple Questions: Extend the program into a quiz that asks for the capitals of 10
#European countries. Provide feedback for each question.

#Advanced Solution:
print("Welcome to the European Capitals Quiz!")
score = 0
questions = {
    "What is the capital of France? ": "paris",
    "What is the capital of Germany? ": "berlin",
    "What is the capital of Italy? ": "rome",
    "What is the capital of Spain? ": "madrid",
    "What is the capital of Portugal? ": "lisbon",
    "What is the capital of Netherlands? ": "amsterdam",
    "What is the capital of Belgium? ": "brussels",
    "What is the capital of Austria? ": "vienna",
    "What is the capital of Switzerland? ": "bern",
    "What is the capital of Greece? ": "athens"
}

for question, correct_answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer.capitalize()}.")

print(f"Your total score is {score} out of {len(questions)}.")


# End of activity