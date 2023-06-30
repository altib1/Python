from Options.LeetManipulator import LeetManipulator


class GetLeetMin(LeetManipulator):
    def __init__(self, words, date):
        super().__init__(words)

    def manipulate(self):
        leet_possibilities = super().manipulate()
        combinations = []
        for possibility in leet_possibilities:
            combinations.append(f"{possibility}")
        return combinations