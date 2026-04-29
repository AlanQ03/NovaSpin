import random

class Slots:
    def __init__(self):
        self.SYMBOLS = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎']

    def spin(self):
        return [random.choice(self.SYMBOLS) for _ in range(3)]
        
    def calculate_payout(self, symbols, bet_amount):
        if symbols[0] == symbols[1] == symbols[2]:
            if symbols[0] == '🍒':
                return bet_amount * 4
            elif symbols[0] == '🍋':
                return bet_amount * 6
            elif symbols[0] == '🍊':
                return bet_amount * 8
            elif symbols[0] == '🍇':
                return bet_amount * 10
            elif symbols[0] == '🔔':
                return bet_amount * 20
            elif symbols[0] == '💎':
                return bet_amount * 50
        elif len(set(symbols)) == 2:
            return bet_amount * 2
        else:
            return -bet_amount