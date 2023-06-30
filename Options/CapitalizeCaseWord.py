from Options.WordManipulator import WordManipulator


class CapitalizeCaseWord(WordManipulator):
    def manipulate_words(self, words):
        capitalized_words = [word.capitalize() for word in words]
        return capitalized_words
    
