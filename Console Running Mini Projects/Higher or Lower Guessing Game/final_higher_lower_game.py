import random
from logo_higher_lower_game import logo , vs
from game_data import data
import sys
sys.path.append("C:\VScode_workspace\python_vscode")
from clear import clear
clear()

def compare(data1,data2,guess,name_list):
    '''this function is to compare the guessed data (i.e) to compare the follower_count '''
    # print("inside compare         ",name_list)
    global end
    global score
    if guess == 'a' and data1['follower_count']>=data2['follower_count'] :
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        print()
        return data1
    elif guess == 'b' and data2['follower_count']>=data1['follower_count']:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        print()
        return data2
    else:
        clear()
        print(logo)
        if guess == "a" and data1['follower_count']<data2['follower_count']:
            print(f"Sorry, that's wrong. {data2['name']} has more followers than {data1['name']} ")
        elif guess == "b" and data2['follower_count']<data1['follower_count']:
            print(f"Sorry, that's wrong. {data1['name']} has more followers than {data2['name']} ")
        print(f"Final Score {score}.")
        end = True
    # print("inside compare inside compare           ",name_list)

def game(previous_data,name_list):
    '''This function is to repeat the process until, it becomes wrong. And to print some data.'''
    # print("inside game          ",name_list)
    global score
    global end
    while end is False:
        random_data_new = random.choice(data)
        # print("first random : ",random_data_new["name"])     # to know the random_data_new["name"]
        if random_data_new["name"] in name_list:
            while random_data_new["name"] in name_list: # if the random_data_new["name"] already in the name_list, then it will run the code until the random_data_new["name"] not in name_list.
                random_data_new = random.choice(data)
                # print("hint",random_data_new)
        name_list.append(random_data_new["name"])
        # print("inside game inside game  ",name_list)
        print(f"Compare A: {previous_data['name']}, a {previous_data['description']}, from {previous_data['country']}")
        print(vs)
        print(f"Against B: {random_data_new['name']}, a {random_data_new['description']}, from {random_data_new['country']}")
        guess = input("Who has more followers in Instagram? Type 'A' or 'B': ").lower()
        previous_data = compare(previous_data,random_data_new,guess,name_list)
        if score >= len(data)-1:
            end = True
            print("You guessed everything right!.")
            break

def start():
    '''This is the function to start the program and if we want to run the program again this function should be called.''' 
    clear()
    print(logo)
    random_data1 = random.choice(data)
    random_data2 = random.choice(data)
    while random_data1 == random_data2:
        random_data2 = random.choice(data)
    print(f"Compare A: {random_data1['name']}, a {random_data1['description']}, from {random_data1['country']}")
    print(vs)
    print(f"Against B: {random_data2['name']}, a {random_data2['description']}, from {random_data2['country']}")
    name_list.append(random_data1["name"])
    name_list.append(random_data2["name"])

    guess = input("Who has more followers in Instagram? Type 'A' or 'B': ").lower()
    previous_data = compare(random_data1,random_data2,guess,name_list)
    game(previous_data,name_list)



score=0
end = False
name_list=[]

start()
# finish = True
while True:
    again = input("Type 'yes' to try again, or type 'no'. : ")
    if again == 'yes':
        score=0
        end = False
        name_list=[]
        start()
    else:
        clear()
        print("Exited.")
        break



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.