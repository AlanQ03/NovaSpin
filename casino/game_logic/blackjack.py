from utils.deck import Deck

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            rank, suit = card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11
            else:
                value += int(rank)
        
        while value > 21 and aces:
            value -= 10
            aces -= 1
        
        return value

    def player_hit(self):
        self.player_hand.append(self.deck.deal())

    def dealer_play(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal())