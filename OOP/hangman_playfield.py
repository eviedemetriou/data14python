from hangman_brain import Brain

word1 = Brain()

while word1.play_again == True:

    word1.hangman_initiation()  # Initializing word to be presented to user
    while word1.game.total_guesses < word1.attempts:
        word1.game.make_guess()  # Make a guess

        if len(word1.game.guess) > 1:  # Case when user chooses to guess the whole word - Check for win/loss
            if word1.game.guess == word1.word:
                word1.hangman_win()
            else:
                word1.hangman_lose()
            break

        word1.hangman_update()  # UPDATE letters in word
        if '_' not in word1.initial_status:  # Check for win
            print(f"Congratulations {word1.user_name}! You won!!!")
            break
        word1.game.update_guess_list()

        if word1.game.total_guesses == word1.attempts - 1:  # Distinct process for the FINAL GUESS of the user
            print("You only have ONE MORE guess.")
            word1.game.make_guess()  # Make a guess

            if len(word1.game.guess) > 1:  # Case when user chooses to guess the whole word - Check for win/loss
                if word1.game.guess == word1.word:
                    word1.hangman_win()
                else:
                    word1.hangman_lose()
                break

            word1.hangman_update()  # UPDATE word with letters
            if '_' not in word1.initial_status:  # Check for win or loss
                print(f"Congratulations {word1.user_name}! You have won!!!")
            else:
                print(f"Sorry {word1.user_name}, you lost!")
            break

    word1.hangman_renew()  # Choice to play again (not working)

