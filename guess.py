# assignment: programming assignment 2
# author: Reed Warren
# date: 10/30/20
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages
from random import randint
done = False  # initialize the while loop flag
print("Play a game: Guess My Number")
while not done:
    my_number = randint(1, 10)  # get a random number from 1 to 10
    print("You have three attempts to guess my number.\n")
    for i in range(3):  # put your code here including a for loop
        if i == 0:
            guess = int(input("Please enter a number from 1 to 10:\n"))
        else:
            guess = int(input("Guess again. Please enter a number:\n"))
        if guess < my_number:
            print("You guessed wrong. Your number is smaller than mine.\n")
        elif guess > my_number:
            print("You guessed wrong. Your number is bigger than mine.\n")
        else:
            print(f"You guessed right. My number is {my_number}. Congratulations you won!\n")
            break
        if i == 2:
            print(f"Sorry, you lost. My number is {my_number}.\n")
    play_again = input("Would you like to play again [Y/N]?\n")
    if play_again == "N" or play_again == "n":
        done = True
print("Goodbye!\n")
