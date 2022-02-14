import random
import hangman_art # here we imported the modules to get the logo and the stages art
import hangman_words # imported the get the list of words to perform

stages=hangman_art.stages
logo=hangman_art.logo
word_list=hangman_words.word_list

chosen_word= random.choice(word_list) # letting the computer to choose the random word
#print(chosen_word)
print(logo)
display=""

list1=[]
for i in range(len(chosen_word)):
    list1+="_" #or    list1.append("_")
print(f"{' '.join(list1)}")  # to print it in list format #print(list1)

exist=[]
new=[] # just to   print("Its already there , type something else")
chances=len(stages)-1
while "_" in list1:
    guess=input("Enter a letter: ").lower()
    if guess not in exist:    
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i]==guess:
                    list1[i]=guess
            print(f"{' '.join(list1)}") # to print it in list format print(list1)
            if guess in new:
                print("It's already there, type something else :)")
            new+=guess
        elif guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life :) ")
            print(stages[chances-1])
            chances-=1
            exist+=guess
    elif guess in exist:
        print("It's already a wrong letter, try another letter.")
    
    if chances==0:
        print("You Lose")
        break
    if "_" not in list1:
        print("You won")
        break














# import random
# from hangman_art import stages, logo
# from hangman_words import word_list
# from replit import clear

# print(logo)
# game_is_finished = False
# lives = len(stages) - 1

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# display = []
# for _ in range(word_length):
#     display += "_"

# while not game_is_finished:
#     guess = input("Guess a letter: ").lower()

#     #Use the clear() function imported from replit to clear the output between guesses.
#     clear()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(f"{' '.join(display)}")

#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             game_is_finished = True
#             print("You lose.")
    
#     if not "_" in display:
#         game_is_finished = True
#         print("You win.")

#     print(stages[lives])