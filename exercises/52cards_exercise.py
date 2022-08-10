import random


class Cards:

    def __init__(self):
        self.types = list('HCDS')
        self.cards = [i for i in range(2, 11)] + list('JQKA')
        self.stack = [(type, card) for type in self.types for card in self.cards]

    def shuffle_stack(self):
        random.shuffle(self.stack)

    def deal_cards(self, q: int):
        self.sample = random.sample(self.stack, q)
        [self.stack.remove(a) for a in self.sample]

    def draw_card(self):
        self.card = self.stack.pop()

    def restore_suffle_stack(self):
        self.stack = Cards().stack
        random.shuffle(self.stack)



c = Cards()
print(c.stack)

c.shuffle_stack()
print(c.stack)

c.deal_cards(10)
print(c.sample)

c.draw_card()
print(c.card)
print(c.stack)

c.restore_suffle_stack()
print(c.stack)
