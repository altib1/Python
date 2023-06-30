import datetime
from Options.CapitalizeCaseWord import CapitalizeCaseWord
from Options.GetLeetMaj import GetLeetMaj
from Options.GetLeetMin import GetLeetMin
from Options.LowerCaseWord import LowerCaseWord
from Options.ManageSpecialChar import ManageSpecialChar

class Engine:
    def __init__(self, words, options):
        self.options = options
        self.words = words
        self.manipulators = []
        self.results = []
        self.array_possibilities = []
        self.initialize_manipulators()
        self.run()

    def initialize_manipulators(self):
        if self.options["leet_min"]:
            word_variations = self.get_word_variations(self.words)
            date_variations = self.get_date_variations()
            for word_variation in word_variations:
                self.manipulators.append(GetLeetMin(word_variation, date_variations))
        if self.options["leet_maj"]:
            self.manipulators.append(GetLeetMaj(self.words))
        if self.options["special_char"]:
            self.manipulators.append(ManageSpecialChar(self.words, self.options))
        if self.options["lowercase"]:
            self.manipulators.append(LowerCaseWord(self.words))
        if self.options["uppercase"]:
            self.manipulators.append(CapitalizeCaseWord(self.words))

    def run(self):
        for manipulator in self.manipulators:
            self.results.extend(manipulator.manipulate())

        date_variations = self.get_date_variations()
        for result in self.results:
            self.array_possibilities.append(result)
            self.array_possibilities.extend([f"{result}{date_variation}" for date_variation in date_variations])

        # Format the results for better readability
        formatted_results = []
        for result in self.array_possibilities:
            formatted_results.append(f"{result}\n")

        self.results = "".join(formatted_results)
        
    @classmethod #Méthode de class
    def get_date_variations(self):
        now = datetime.datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")
        year_short = now.strftime("%y")
        month_name = now.strftime("%B")
        month_abbr = now.strftime("%b")

        return [day, month, year, year_short, month_name, month_abbr]

    def get_word_variations(self, words):
        variations = []
        for word in words:
            # Add the original word
            variations.append(word)
        
            # Add capitalized variation
            variations.append(word.capitalize())
        
            # Add more variations as needed
        
        return variations

    def get_results(self):
        return self.results
