#   Level Three Guessing Game

#   In level three, the computer's guesses are 
#   optimized to refine the range on the guesses 
#   based on whether they are too high or too low. 
#   Print how many guesses it takes computer before 
#   it correctly guesses the number.

# ----------------------------------------------------------------------
# import random

# guessesTaken = 0

# print('The computer will try to guess your number with the fewest amount of gueses.')
# player_number = input('Please pick a number between 1 and 10:  ' )
# player_number = int(player_number)

# while guessesTaken < 6:
#     guess = random.randint(1, 10)
#     guess = int(guess)

#     guessesTaken = guessesTaken + 1

#     if guess < player_number:
#         print('The computers guess is too low.') 

#     if guess > player_number:
#         print('The computers guess is too high.')

#     if guess == player_number:
#         break

# if guess == player_number:
#     guessesTaken = str(guessesTaken)
#     print('The computer guessed my number in ' + guessesTaken + ' guesses!')



from random import randint

print ("In this program you will enter a number between 1 - 100."
       "\nAfter the computer will try to guess your number!")

number = 0

while number < 1 or number >100:
    number = int(input("\n\nEnter a number for the computer to guess: "))
    if number > 100:
        print ("Number must be lower than or equal to 100!")
    if number < 1:
        print ("Number must be greater than or equal to 1!")

guess = randint(1, 100)

print ("The computer takes a guess...", guess)

while guess != number:
    if guess > number:
        guess -= 1
        guess = randint(1, guess)
    else:
        guess += 1
        guess = randint(guess, 100)
    print ("The computer takes a guess...", guess)

print ("The computer guessed", guess, "and it was correct!")