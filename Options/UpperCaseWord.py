class UpperCaseWord:
    def __init__(self, words):
        self.words = words
        self.possibilities = self.convert_to_upper_case()

    def convert_to_upper_case(self):
        return [word.upper() for word in self.words]
    