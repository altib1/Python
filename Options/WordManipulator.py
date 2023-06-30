from ManipulatorInterface import ManipulatorInterface


class WordManipulator(ManipulatorInterface):
    def __init__(self, words):
        self.words = words
        self.possibilities = []

    def transform(self):
        pass