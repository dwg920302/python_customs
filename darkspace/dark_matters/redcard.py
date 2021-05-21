class Card(object):
    def __init__(self, number):
        self.number = number
        self.light = 0


class LightCard(Card):
    def __init__(self, number):
        self.number = number
        self.light = 1


class RedCard(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        deck = []



RedCard.main()
