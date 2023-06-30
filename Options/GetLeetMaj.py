from Options.LeetManipulator import LeetManipulator


class GetLeetMaj(LeetManipulator):
    @staticmethod
    def get_leet_variation(word):
        leet_mapping = {
            'a': '4',
            'e': '3',
            'g': '6',
            'l': '1',
            'o': '0',
            's': '5',
            't': '7'
        }

        leet_word = ''
        for char in word:
            leet_char = leet_mapping.get(char.lower(), char)
            leet_word += leet_char

        return leet_word.upper()

    def manipulate_words(self, words):
        manipulated_words = []
        for word in words:
            leet_variation = self.get_leet_variation(word)
            manipulated_words.append(leet_variation)
        return manipulated_words
