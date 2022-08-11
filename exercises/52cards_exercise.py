import random


class Stack:

    def __init__(self):
        self.types = list('HCDS')
        self.cards = [i for i in range(2, 11)] + list('JQKA')
        self.stack = [(type, card) for type in self.types for card in self.cards]

    def shuffle_stack(self):
        random.shuffle(self.stack)

    def deal_cards(self, q: int):
        self.sample = random.sample(self.stack, q)
        [self.stack.remove(a) for a in self.sample if len(self.stack) > 0]

    def draw_card(self):
        if len(self.stack) > 0:
            self.card = self.stack.pop()
        else: return print('There are not more cards in the stack')

    def restore_suffle_stack(self):
        self.stack = Stack().stack
        random.shuffle(self.stack)


if __name__ == '__main__':
    c = Stack()
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
