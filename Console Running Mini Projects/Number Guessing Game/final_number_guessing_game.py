import sys
sys.path.append("C:\VScode_workspace\python_vscode")
from clear import clear
import random
from logo_number_game import logo

def difficulty():
    '''function to find the difficulty by user input'''
    global attempt
    end=False
    while end is False:
        difficulty=input("Choose difficulty, Type 'Easy' or 'Hard' : ").lower()
        if difficulty=='easy':
            attempt=10
            end=True
        elif difficulty=='hard':
            attempt=5
            end=True
        else:
            print("Type a valid difficulty level.")
    return attempt

def guess_check(attempt):
    '''function to check the guessed number with the actual number'''
    while attempt!=0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))

        if guess != number:
            if guess not in guess_list:
                attempt-=1
            else:
                print("You have already typed this number.")
        elif guess == number:
            print()
            print("You guessed it RIGHT.")
            print("YOU WON :)")
            break
        guess_list.append(guess)
        # print(guess_list)
        
        hint(attempt,guess) # calling hint() function

def hint(attempt,guess):
    '''function to give some hints for the player to guess the correct number'''
    if guess < number:
        if abs(number-guess) < 5:
            print(f"You are too close and the {guess} is lower than actual number.") 
        else:
            print(f"{guess} is LOWER than actual number.")
    elif guess > number:
        if abs(guess-number) < 5:
            print(f"You are too close and the {guess} is higher than actual number.") 
        else:
            print(f"{guess} is HIGHER than the actual number.")

    if abs(guess-number) == 1:
        attempt += 1
    if attempt >= 1:
        print("Guess again")
    if attempt<1:
        print()
        print("You have run out of guesses, YOU LOSE :( ")


clear()
print(logo)
number = random.randint(1,100)
print("The number is between 1 and 100.")
attempt = 0
guess_list=[]


difficulty() # calling difficulty() function
guess_check(attempt) # calling guess_check() function

