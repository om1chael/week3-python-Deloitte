# fog=7
# happy=15

import Scrabble_Checker
import pytest

s = Scrabble_Checker.ScrabbleChecker()


@pytest.mark.parametrize("test_word,expected",
                         [
                             ("quit", True),
                             ("happy", False),
                             ("..';;", False),
                             ("abab", False),
                         ])
def test_quit_function(test_word, expected):
    assert s.quit_game(test_word) == expected


@pytest.mark.parametrize("test_word,expected",
                         [
                             ("help", True),
                             ("happy", True),
                             ("car", True),
                             ("abc", False),
                             ("abab", False),
                         ])
def test_word(test_word, expected):
    assert s.input_check(test_word) == expected

@pytest.mark.parametrize("word,expected",
                         [
                            ("oo", True),
                            ("abc", False),
                            ("razor",False)
                         ])
def test_checker(word,expected):
    s.letters = "razooo"
    assert s.letter_check(word) == expected

@pytest.mark.parametrize("word,expected",
                         [
                            ("oo", True),
                            ("abc", False),
                            ("razor",False)
                         ])
def test_checker(word,expected):
    s.letters = "razooo"
    assert s.letter_check(word) == expected
