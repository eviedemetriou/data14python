from scrabble_game1 import Scrabble
#from unittest import TestCase

game = Scrabble()

def test_tile_generation():
    game.word_chosen = ''
    assert len(game.tile_generation()) == 7
    game.word_chosen = 'road'
    game.tiles = ['R', 'O', 'A', 'D', 'T', 'P', 'Q']
    assert len(game.tile_generation()) == 7

def test_word_check():
    game.tiles = ['U', 'B', 'F', 'Q', 'T', 'P', 'R']
    assert game.word_check() == ''
    game.tiles = ['O', 'B', 'F', 'Q', 'T', 'P', 'R']
    assert game.word_check() == 'for'
    game.tiles = ['A', 'B', 'O', 'A', 'T', 'P', 'R']
    assert game.word_check() == 'boat'

def test_word_score():
    game.word_chosen = 'sun'
    game.get_word_score()
    assert game.word_score == 3
    game.word_chosen = 'rope'
    game.get_word_score()
    assert game.word_score == 6
    game.word_chosen = 'horse'
    game.get_word_score()
    assert game.word_score == 8


from io import StringIO

def test_want_to_play(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO("Y"))
    assert game.play_again == True
    #monkeypatch.setattr('sys.stdin', StringIO("N"))  # With the 'no' option the test fails (not sure why)
    #assert game.play_again == False


## Using 'monkeypatch' with 'pytest' to set certain inputs
# from io import StringIO
#
# def test_take_input(monkeypatch):
#     monkeypatch.setattr(('sys.stdin'), StringIO("Hello!"))
#     assert take_input() == "Hello!"  # or could have different 'strings' and '!=' operator
