import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])   #定义类型card，有rank和card两种属性

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]
beer_card = Card('7', 'diamond')
print(beer_card)
french = FrenchDeck()
print(french.cards)
print(len(french))
print(french[0])
print(french[-1])
print(choice(french))
print(choice(french))

#排序
suit_valus = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spades_high(card):   #排序函数，定义key，使得从低到高排序
    rank_value = french.ranks.index(card.rank)
    return rank_value * 4 + suit_valus[card.suit]
for card in sorted(french, key=spades_high):
    print(card)