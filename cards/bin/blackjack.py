#!/usr/bin/env python3
import numpy as np
from card_deck import deck
np.random.seed(0)

class blackjack(object):
    ''' an object which plays a single hand of blackjack against the dealer
    '''
    def __init__(self):
        self.deck_ = deck()
        self.card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8,
                                      9:9, 10:10, 11:10, 12:10, 13:10}
        self.result = self.play_hand()

    def play_hand(self):
        # NOTE: 0 = player win, 1 = dealer win, 2 = draw
        player_hand = self.deck_.deal(2)
        player_score = self.score_hand(player_hand)
        print('players turn')
        while player_score < 17:
            print(' - hit')
            player_hand.append(self.deck_.deal(1)[0])
            player_score = self.score_hand(player_hand)
            print(' - current score:', player_score)
        if player_score > 21:
            print(' - bust')
            return 1

        dealer_hand = self.deck_.deal(2)
        dealer_score = self.score_hand(dealer_hand)
        print('dealers turn')
        while dealer_score < 17:
            print(' - hit')
            dealer_hand.append(self.deck_.deal(1)[0])
            dealer_score = self.score_hand(dealer_hand)
            print(' - current score:', dealer_score)
        if dealer_score > 21:
            print(' - bust')
            return 0

        if player_score > dealer_score:
            return 0
        elif dealer_score > player_score:
            return 1
        else:
            return 2

    def score_hand(self, hand):
        score = 0
        for card in hand:
            score += card[0]
        return score

def main():
    wins_dealer = 0
    wins_player = 0
    draws = 0
    num_trials = 100000
    for i in range(num_trials):
        trial = blackjack()
        result_ = trial.result
        if result_ == 0:
            wins_player += 1
        elif result_ == 1:
            wins_dealer += 1
        else:
            draws += 1

    print(wins_dealer, wins_player, draws)

if __name__ == '__main__':
    main()
