#!/usr/bin/env python3
import numpy as np
from card_deck import deck
np.random.seed(0)

class blackjack(object):
    ''' an object which plays a single hand of blackjack against the dealer
    '''
    def __init__(self):
        deck_ = deck()
        print(deck_)



def main():
    blackjack_ = blackjack()

if __name__ == '__main__':
    main()
