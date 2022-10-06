class Person:
    mots = []
    dates = []

    def __init__(self, mots, dates):
        self.mots = mots
        self.dates = dates

    def dates(self):
        return self.dates

    def mots(self):
        return self.mots
