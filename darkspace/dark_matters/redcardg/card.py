class Card(object):
    light = False
    spec = 0

    def __init__(self, number, name):
        self.number = number
        self.name = name


class LightCard(Card):
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.light = True
        self.spec = 0


class SpecCard(Card):
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.light = False
        self.spec = number
