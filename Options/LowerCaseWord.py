from Options.WordManipulator import WordManipulator


class LowerCaseWord(WordManipulator):
    def manipulate_words(self, words):
        lowercased_words = [word.lower() for word in words]
        return lowercased_words