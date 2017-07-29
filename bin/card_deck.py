#!/usr/bin/env python3
import numpy as np

class deck(object):
    ''' an object which holds a deck of cards. ace=1, 2=2, ..., q=12, k=13.
    it can shuffle and deal n cards. '''
    def __init__(self, start_shuffled = True):
        self.suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self.values = np.arange(1,14)
        self.cards = {}
        self.current_state = []
        card_id = 0
        for suit in self.suits:
            for value in self.values:
                self.cards[card_id] = [value, suit]
                self.current_state.append([value, suit])
                card_id += 1
        if start_shuffled:
            self.shuffle()

    def shuffle(self):
       num_cards = len(self.suits) * len(self.values)
       card_indices = np.arange(num_cards)
       np.random.shuffle(card_indices)
       shuffled_deck = []
       for index in card_indices:
           shuffled_deck.append(self.cards[index])
       self.current_state = shuffled_deck

    def deal(self, num_cards):
        if num_cards > 52:
            raise ValueError('can\'t deal that many cards')
        else:
            hand = []
            for i in range(num_cards):
                card = self.current_state.pop()
                hand.append(card)
            return hand

    def get_state(self):
        return self.current_state

    def __str__(self):
        return str(self.current_state)

def main():
    np.random.seed(0)
    deck_ = deck()

if __name__ == '__main__':
    main()
