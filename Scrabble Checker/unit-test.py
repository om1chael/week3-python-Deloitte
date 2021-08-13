# fog=7
# happy=15

from Scrabble_Checker import Scrabble_Checker
import pytest
s = Scrabble_Checker()
@pytest.mark.parametrize("test_word,expected",
[
    ("quit",True),
    ("abc", False),
    ("abab", False),
])
def test_quit_function(test_word,expected):
    assert s.quit_game(test_word)==expected

@pytest.mark.parametrize("test_word,expected",
[
    ("help",True),
    ("car",True),
    ("abc", False),
    ("abab", False),
])

def test_word(test_word,expected):
    assert s.input_check(test_word) == expected

@pytest.mark.parametrize("word,expected",
[
    ("fog",7)
])

def test_word(word,expected):

    assert s.score_update(word) == s.user_score

### test for
