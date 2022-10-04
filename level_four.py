#   Level Four Guessing Game

#   In level four, give the user an option to play 
#   against the computer or to think of a number for 
#   the computer to guess.

# ----------------------------------------------------------------------

from level_one import user_playing
from level_three import computer_playing

player_choice = int(input('Choose to guess the computers number or pick a number for the computer to guess! Type "1" to guess and "2" to pick. '))

if player_choice == 1:
    user_playing()
elif player_choice == 2:
    computer_playing()
else:
    print('Please enter a valid response.')