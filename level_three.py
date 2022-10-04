#   Level Three Guessing Game

#   In level three, the computer's guesses are 
#   optimized to refine the range on the guesses 
#   based on whether they are too high or too low. 
#   Print how many guesses it takes computer before 
#   it correctly guesses the number.

# ----------------------------------------------------------------------

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