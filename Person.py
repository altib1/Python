from datetime import datetime


class Person:
    mots = []
    dates = []
    todays_date = datetime.today()

    def __init__(self, mots, dates):
        self.mots = mots
        self.dates = dates

    def day(self):
        return self.todays_date.day

    def month(self):
        return self.todays_date.month

    def year(self):
        return self.todays_date.year

    def mots(self):
        return self.mots
