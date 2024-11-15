#!/usr/bin/env python3

'''
Project 1 - Number Guessing Game
--------------------------------

'''
import random

def start_game():
    # Game banner
    print('-' * 24)
    print('| Number Guessing Game |')
    print('-' * 24)
    
    # Generate a random number from 1 - 10
    random_number = random.randint(1, 10)
    print('Guess a number between 1 - 10')
    incorrect_guess = 0
    
    while True:
        try:
            guess = int(input('Guess the random number? '))
            if guess > 10:
                raise ValueError('Only numbers from 1-10')
        except ValueError as err:
            print(f'Please enter a number between 1-10. ')
            print(err)
        else:
            if guess == random_number:
                print('Correct! You guessed right.')
                break
            elif guess < random_number:
                incorrect_guess += 1
                print('Incorrect, guess higher')
            elif guess > random_number:
                incorrect_guess += 1
                print('Incorrect, guess lower')
    print(f'You took {incorrect_guess} try to get it right.')

# start the game
start_game()

play_again = input('Would you like to play again [y]es/[n]o? ')
if play_again.lower() == 'y':
    start_game()
else:
    print('Thanks for playing')
    break
    

