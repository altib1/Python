import itertools
from Options.WordManipulator import WordManipulator


class ManageSpecialChar(WordManipulator):
    def __init__(self, words, options):
        super().__init__(words)
        self.options = options
        self.common_special_chars = '.$?!*'
        self.all_special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>/?'

    def manipulate(self):
        combinations = []
        chars_to_use = self.common_special_chars if self.options["special_char_level"] == "common" else self.all_special_chars
        for word in self.words:
            word_combinations = [word]
            for i in range(1, min(self.options["special_char_max"], len(word) + 1)):
                word_combinations.extend([''.join(comb) for comb in itertools.combinations(word, i)])
            word_combinations.extend([word + char for char in chars_to_use])
            combinations.append(word_combinations)
        return list(set(itertools.chain(*combinations)))


