from Options.WordManipulator import WordManipulator


class CapitalizeCaseWord(WordManipulator):
    def __init__(self, words):
        super().__init__(words)
    #Polymorphisme    
    def run(self):
        return [word.capitalize() for word in self.words]
    
