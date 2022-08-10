import random


class Cards:

    def __init__(self):
        self.types = list('HSCD')
        self.cards = [i for i in range(2, 11)] + list('JQKA')
        self.deck = [(type, card) for type in self.types for card in self.cards]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self, q: int):
        self.sample = random.sample(self.deck, q)
        [self.deck.remove(a) for a in self.sample]

    def draw_card(self):
        self.card = self.deck.pop()

    def restore_suffle_deck(self):
        self.deck = Cards().deck
        random.shuffle(self.deck)



c = Cards()
print(c.deck)

c.shuffle_deck()
print(c.deck)

c.deal_cards(10)
print(c.sample)

c.draw_card()
print(c.card)
print(c.deck)

c.restore_suffle_deck()
print(c.deck)
