import random


class Stack:

    def __init__(self):
        self.types = list('HCDS')
        self.cards = [str(i) for i in range(2, 11)] + list('JQKA')
        self.stack = [(type, card) for type in self.types for card in self.cards]

    def shuffle_stack(self):
        random.shuffle(self.stack)

    def add_card_to_stack(self):
        categories = {1: 'H', 2: 'C', 3: 'D', 4: 'S'}
        menu1 ='\n 1: hearths\n 2:Clubs \n 3:Diamonds \n 4:Spades '
        category, number, card = '', '', ''

        while category not in categories and number not in self.cards :
            category = input(f'\n select type of stack: \n options: {menu1} \n')
            number = input(f'\n select value :  {self.cards}\n ')
            card = (categories[int(category)], number)
            self.stack.remove(('C', '2'))

        while card in self.stack:
                print('card already exists in stack...')
                category = input(f'select type of stack: \n options: {menu1} \n')
                number = input(f'select value :  {self.cards}\n ')
                card = (categories[int(category)], number)

        else:
            self.stack.append((categories[int(category)], number))

    def deal_cards(self, q: int):
        self.sample = random.sample(self.stack, q)
        [self.stack.remove(a) for a in self.sample if len(self.stack) > 0]

    def draw_card(self):
        if len(self.stack) > 0:
            self.card = self.stack.pop()
            self.sample.append(self.card)
        else:
            return print('There are not more cards in the stack')

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
    print(c.sample)

    c.restore_suffle_stack()
    print(c.stack)

    c.add_card_to_stack()
