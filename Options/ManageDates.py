from datetime import datetime

class ManageDates:

    def __init__(self, date):
        self.date = datetime(date.year, date.month, date.day)

    def run(self):
        self.date
        pass

    def day(self):
        return self.date.day

    def month(self):
        return self.date.month

    def year(self):
        return self.date.year
    
    @staticmethod # Méthode statique
    def getMonthName(month):
        return datetime(2000, month, 1).strftime('%B')