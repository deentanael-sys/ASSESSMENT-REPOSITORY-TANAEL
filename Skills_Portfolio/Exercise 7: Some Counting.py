#Instructions Given:
'''
Use your newly acquired knowledge of the for loop to complete the following tasks. Print
all values to the console in each case.
1. Write a loop that counts up from 0 to 50 in increments of 1.
2. Write a loop that counts down from 50 to 0 in decrements of 1.
3. Write a loop that counts up from 30 to 50 in increments of 1.
4. Write a loop that counts down from 50 to 10 in decrements of 2.
5. Write a loop that counts up from 100 to 200 in increments of 5. 
You may include all loops in a single project
'''
def loop1():
    for x in range(0, 51, 1): #counts up from 0 to 50 in increments of 1, solves task 1
        print(x)
    print('loop that counts up from 0 to 50 in increments of 1')

def loop2():
    for y in range(50, -1, -1): #counts down from 50 to 0 in decrements of 1, solves task 2
        print(y)
    print('loop that counts down from 50 to 0 in decrements of 1')

def loop3():
    for z in range(30, 51, 1): #counts up from 30 to 50 in increments of 1, solves task 3
        print(z)
    print('loop that counts up from 30 to 50 in increments of 1')

def loop4():
    for w in range(50, 9, -2): #counts down from 50 to 10 in decrements of 2, solves task 4
        print(w)
    print('loop that counts down from 50 to 10 in decrements of 2')

def loop5():
    for v in range(100, 201, 5): #counts up from 100 to 200 in increments of 5, solves task 5
        print(v)
    print('loop that counts up from 100 to 200 in increments of 5')
        
#in addition I made each into a function so you can choose which one to run

def tasks():
    inputloop = int(input("Which loop would you like to run? (1-5): ")) #asks user which loop to run
    if inputloop == 1:
        loop1()
    elif inputloop == 2:
        loop2()
    elif inputloop == 3:
        loop3()
    elif inputloop == 4:
        loop4()
    elif inputloop == 5:
        loop5()
    else:
        print("Invalid input. Please enter a number between 1 and 5.") #invalid input handling
        tasks() #loops back to ask again if invalid input

tasks() #starts program

# End of activity