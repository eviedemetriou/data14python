from scrabble_game1 import Scrabble
#from unittest import TestCase

game = Scrabble()

    def test_tile_generation(self):
        game.word_chosen == ''
        assert len(game.tile_generation()) == 7
        game.word_chosen == 'ab'
        assert len(game.tile_generation()) == 7

    def test_word_check():
        game.tiles == ['U', 'B', 'F', 'Q', 'T', 'P', 'R']
        assert game.word_check() == ''
        game.tiles == ['O', 'B', 'F', 'Q', 'T', 'P', 'R']
        assert game.word_check() == 'to'
        game.tiles == ['A', 'B', 'O', 'A', 'T', 'P', 'R']
        assert game.word_check() == 'boat'

    def test_word_score():
        game.word_chosen = 'sun'
        #assert game.word_score == 3
        assert f"This word is worth {game.word_score} points.\n"
        game.word_chosen = 'rope'
        #assert game.word_score == 6
        assert f"This word is worth {game.word_score} points.\n"

    # def test_want_to_play():
    #     if choice == 'y':
    #         assert game.play_again == True
    #     if choice == 'n':
    #         assert game.play_again == False


## Using 'monkeypatch' with 'pytest' to set certain inputs
# from io import StringIO
#
# def test_take_input(monkeypatch):
#     monkeypatch.setattr(('sys.stdin'), StringIO("Hello!"))
#     assert take_input() == "Hello!"  # or could have different 'strings' and '!=' operator
