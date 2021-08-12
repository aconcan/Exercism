# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self._word = word

        # track guesses already made 
        self._guesses = set()


    def guess(self, char):
        # check game status
        if self.status != STATUS_ONGOING:
            raise ValueError('No guesses left bud')
        
        # add guess to set if not already there
        if char not in self._guesses and char in self._word:
            self._guesses.add(char)

            # check for a win
            if all(letter in self._guesses for letter in self._word):
                self.status = STATUS_WIN
        
        # if not win decrement guess and check for a loss
        else:
            self.remaining_guesses -= 1
            print(self.remaining_guesses)
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
                

    def get_masked_word(self):
        return ''.join(c if c in self._guesses else '_' for c in self._word)

    def get_status(self):
        return self.status
