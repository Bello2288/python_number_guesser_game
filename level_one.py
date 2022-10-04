#   Level One Guessing Game

#   In level one, the computer generates a random number 
#   between 1 and 10 and the user has 3 guesses to pick 
#   the correct number. The computer will tell you if you 
#   are too high or too low.

# ----------------------------------------------------------------------
import random


guessesTaken = 0

number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')

while guessesTaken < 3:
    print('You have three guesses to get it right. What is your guess.') 
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') 
    
    if guess > number:
        print('Your guess is too high.')
    
    if guess == number:
        break
    
if guess == number:
   print('Good job! You guessed my number!')
    
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)