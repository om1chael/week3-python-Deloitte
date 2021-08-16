import string
import random
import enchant
from Scrabble_Data import letter_scores


class ScrabbleChecker:
    def __init__(self):
        self.user_score = 0
        self.letters = ""

    # sets up the letters of the board
    def current_board(self):
        self.letters = self.letter_generation()

    # returns a random character from alphabet
    def random_generation(self):
        return random.choice(string.ascii_lowercase)

    # fills an array with random letters
    def letter_generation(self) -> list:
        word = []
        for i in range(10):
            word.append(self.random_generation())
        return word

    def input_check(self, word: str) -> bool:
        """ Check if the word actually exists in a dict.
          Looks at the letters in the word and scores them.
          Adds ups the scores for each letter if the previous checks have been done"""
        if self.eng_dict(word) == True and self.letter_check(word) == True:
            self.change_letters(word)
            self.score_update(word)
        else:
            return False
        return True

    # Checks the users letter with the random letters given to him
    def letter_check(self, word) -> bool:
        list_word=" ".join(self.letters).split()
        for letter in word:
            if letter not in list_word:
                return False
            else:
                list_word.remove(letter)
        return True

    # quit game if user types "quit"
    def quit_game(self, user_input: str) -> bool:
        return user_input == "quit"

    # replaces picked letters by user
    def change_letters(self, word):
        for letter in word:
            if letter in self.letters:
                self.letters[self.letters.index(letter)] = self.random_generation()

    # updates the users score with the users word
    def score_update(self, word: str) -> int:
        for i in word:
            self.user_score = self.user_score + letter_scores[i]
        return self.user_score

    # checks if the input word is valid
    def eng_dict(self, word: str) -> bool:
        if len(word) <= 2:
            return False
        dict_style = enchant.Dict("en_US")
        valid_word = dict_style.check(word)
        if not valid_word:
            print("\n ################################")
            print(f" ### Sorry '{word}' is Not A word ###")
            print(" ################################")
            return valid_word
        return True
