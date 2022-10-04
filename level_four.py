#   Level Four Guessing Game

#   In level four, give the user an option to play 
#   against the computer or to think of a number for 
#   the computer to guess.

# ----------------------------------------------------------------------

# from level_one import user_guess
# from level_three import computer_guess

import random

player_choice = int(input('Choose to guess the computers number or pick a number for the computer to guess! Type "1" to guess and "2" to pick. '))

if player_choice == 1:
    # user_guess()
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


elif player_choice == 2:
    # computer_guess()
    def computer_guess(number):
        guessesTaken = 0

        low = 1
        high = 100
        guess = (low+high)//2
        while guess != number:

            guessesTaken = guessesTaken + 1

            guess = (low+high)//2
            
            if guess > number:
                high = guess
                print("The computer takes a guess...", guess, "is too high.")
            elif guess < number:
                low = guess + 1
                print("The computer takes a guess...", guess, "is too low.")

        print("The computer guessed", guess, "and it was correct!")


    def main():
        number = int(input("Enter a number between 1 and 100: "))
        if number < 1 or number > 100:
            print("Must be in range [1, 100]")
        else:
            computer_guess(number)

    if __name__ == '__main__':
        main()



else:
    print('Please enter a valid response.')