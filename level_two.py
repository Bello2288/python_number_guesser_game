#   Level Two Guessing Game

#   In level two, the game is reversed and the 
#   user picks a number and the computer then has 
#   3 guesses to select the correct answer.

# ----------------------------------------------------------------------
import random

guessesTaken = 0

print('The computer has three tries to guess your number.')
player_number = input('Please pick a number between 1 and 10:  ' )
player_number = int(player_number)

while guessesTaken < 3:
    guess = random.randint(1, 10)
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1

    if guess < player_number:
        # guess = str(guess)
        print('The computers guess is too low. The computer guessed ',guess) 
    
    if guess > player_number:
        # guess = str(guess)
        print('The computers guess is too high. The computer guessed ',guess)
    
    if guess == player_number:
        break
    
if guess == player_number:
   print('The computer guessed your number!')
    
if guess != player_number:
    print('Nope. The computer did not guess your number!')

