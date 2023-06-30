from Options.WordManipulator import WordManipulator


class LeetManipulator(WordManipulator):
    def __init__(self, words):
        super().__init__(words)
        self.leet_table = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            'l': '1',
            's': '5',
            'b': '8',
            't': '7',
            'z': '2',
            'g': '6'
        }

    def manipulate(self):
        combinations = []
        for word in self.words:
            word_combinations = []
            for char in word:
                if char.lower() in self.leet_table:
                    word_combinations.append(self.leet_table[char.lower()].upper())
                else:
                    word_combinations.append(char)
            combinations.append(''.join(word_combinations))
        return combinations