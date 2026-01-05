#Instructions Given:
'''
Write a program that tells a user how many days there are in a specific month. Use a
dictionary to map the month numbers (1-12) to the number of days in each month.
'''
#Steps:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and names and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

#Simple Solution:
'''
daysinmonth = { #defined dictionary that lists number of days in each month completes 1st task
    1: "January has 31 days",
    2: "February has 28 days",
    3: "March has 31 days",
    4: "April has 30 days",
    5: "May has 31 days",
    6: "June has 30 days",
    7: "July has 31 days",
    8: "August has 31 days",
    9: "September has 30 days",
    10: "October has 31 days",
    11: "November has 30 days",
    12: "December has 31 days"
}

def days_in_month(): #made into function so I can loop it if there's an invalid input
    month = int(input("Enter month number (1-12): ")) #asks input from user completes 2nd task
    if month in daysinmonth:
        print(f"{daysinmonth[month]}")
    else: #invalid input handling completes 3rd task
        print("Invalid month number. Please enter a number between 1 and 12.") 
        days_in_month() #here's the loop if invalid input

days_in_month() #calling the function
'''
#Advanced Requirement:
#1. Leap Year Adjustment: Modify the program to account for leap years. For February, ask
#2. the user if the year is a leap year and adjust the number of days accordingly.

#Advanced Solution:
daysinmonth = { #defined dictionary that lists number of days in each month normally
    1: "January has 31 days",
    2: "February has 28 days",
    3: "March has 31 days",
    4: "April has 30 days",
    5: "May has 31 days",
    6: "June has 30 days",
    7: "July has 31 days",
    8: "August has 31 days",
    9: "September has 30 days",
    10: "October has 31 days",
    11: "November has 30 days",
    12: "December has 31 days"
}

leapyear = input("Is it a leap year? (yes/no): ").strip().lower() #asks if it's a leap year solves task 1
if leapyear == "yes":
    daysinmonth[2] = "February has 29 days since it's a leap year" #Edits number of days in February if leap year solves task 1

#same function as in simple solution
def days_in_month(): 
    month = int(input("Enter month number (1-12): ")) 
    if month in daysinmonth:
        print(f"{daysinmonth[month]}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.") 
        days_in_month() 

days_in_month()
# End of activity