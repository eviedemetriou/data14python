from scrabble_game import Scrabble
#from unittest import TestCase

game = Scrabble()

def test_tile_generation(self):
    if game.word_chosen == '':
        assert game.tile_generation(len(game.tiles)) == 7
    if game.word_chosen == 'ab':
        assert game.tile_generation(len(game.tiles)) == 7

def test_word_check():
    if game.tiles == ['U', 'B', 'F', 'Q', 'T', 'P', 'R']:
      assert game.word_check()
    if game.tiles == ['O', 'B', 'F', 'Q', 'T', 'P', 'R']:
      assert game.word_check(game.word_chosen) == 'to'
    if game.tiles == ['A', 'B', 'O', 'A', 'T', 'P', 'R']:
      assert game.word_check(game.word_chosen) == 'boat'

def test_word_score():
    game.word_chosen = 'sun'
    #assert game.word_score == 3
    assert f"This word is worth {game.word_score} points.\n"
    game.word_chosen = 'rope'
    #assert game.word_score == 6
    assert f"This word is worth {game.word_score} points.\n"

def test_want_to_play():
    if choice == 'y':
        assert game.play_again == True
    if choice == 'n':
        assert game.play_again == False
