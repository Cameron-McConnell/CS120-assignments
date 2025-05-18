"""
Cameron McConnell
05/18/2025
Number Guesser

This is a simple number guesser game.
The computer randomly selects a number,
then the user has up to 7 tries to guess
the correct number. After each guess, the
program tells the user if the guess is too,
low or too high, or correct. Invalid inputs
(non numbers) count as a try. The game will
end when the user guesses correctly or uses
all 7 tries.
"""

import random

def number_guesser():
    secretNumber = random.randint(1, 100)
    
    maxTries = 7
    currentTries = 0
    guessedCorrectly = False
    keepGoing = True
    
    while keepGoing:
        print("Enter a number between 1 and 100: ")
        userInput = input()
        currentTries += 1
        
        if userInput.isdigit():
            guess = int(userInput)
            
            if guess < secretNumber:
                print("Too low")
            elif guess > secretNumber:
                print("Too high")
            else:
                print(f"Correct! You guessed the number in {currentTries} tries.")
                guessedCorrectly = True
                keepGoing = False
                
        else:
            print("Invalid input. This counts as a try. ")
        
        
        if currentTries == maxTries and not guessedCorrectly:
            keepGoing = False
            
            
    if not guessedCorrectly:
        print(f"Sorry, you lost. The correct number was {secretNumber}. ")
        

number_guesser()
