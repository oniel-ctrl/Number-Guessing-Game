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

    incorrect_guess = 0
    random_number = random.randint(1, 10)
    high_score(incorrect_guess)
    print('Guess a number between 1 - 10')
    
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
    high_score(incorrect_guess)
    question = input('Would you like to play again [y]es/[n]o? ')

    play_again(question)

def play_again(answer):
    if answer.lower() == 'y':
        start_game()
    else:
        print('Thanks for playing')

# High score
def high_score(score):
    new_high_score = 0
    if new_high_score < score:
        new_high_score = score
        print(f'New High Score: {new_high_score}')
    else:
        print(f'High Score: {new_high_score}')

# start the game
start_game()

  

