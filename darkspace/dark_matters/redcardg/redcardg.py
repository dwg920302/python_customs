from card import *


class RedCardG(object):

    @staticmethod
    def main():
        deck = []
        for i in range(2):
            for j in range(10):
                j += 1
                if i % 2 != 0:
                    if j == 1 or j == 3 or j == 8:
                        deck.append(LightCard(j, f'[Light {j}]'))
                    elif j == 4 or j == 7:
                        deck.append(SpecCard(j, f'[Special {j}]'))
                    else:
                        deck.append(Card(j, f'[Normal {j}]'))
                else:
                    deck.append(Card(j, f'[Normal {j}]'))

        for i in deck:
            print(i.name)


RedCardG.main()
