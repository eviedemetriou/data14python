from hangman_brain import Brain
from hangman_game import Game

game1 = Game()
word1 = Brain()
while game1.total_guesses < 5:
    word1.hangman_initiation()
#    game1.guess = input("Make a guess:  \n")
#     while game1.guess in game1.guesses_list:
#         guess = input(f"You have already used {game1.guess}. Make another guess:  \n")
#     print(game1.update_guess_list(guess))
#     print(f"You made {game1.total_guesses} guess(es) so far!")
#
#     if game1.total_guesses == 4:
#         guess = input("Make your final guess:  \n")
#         while guess in game1.guesses_list:
#             guess = input(f"You have already used {guess}. Make another guess:  \n")
#
#         game1.total_guesses = 5
#         print("You have made the max number of guesses allowed.")

word1 = Brain()
word1.hangman_initiation()
