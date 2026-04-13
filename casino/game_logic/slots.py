import random

class Slots:
    def __init__(self):
        self.SYMBOLS = ['cherry', 'lemon', 'orange', 'plum', 'bell', 'bar']

        def spin(self):
            return [random.choice(self.SYMBOLS) for _ in range(3)]
        
        def calculate_payout(self, symbols, bet_amount):
            if symbols[0] == symbols[1] == symbols[2]:
                if symbols[0] == 'cherry':
                    return bet_amount * 10
                elif symbols[0] == 'lemon':
                    return bet_amount * 20
                elif symbols[0] == 'orange':
                    return bet_amount * 30
                elif symbols[0] == 'plum':
                    return bet_amount * 40
                elif symbols[0] == 'bell':
                    return bet_amount * 50
                elif symbols[0] == 'bar':
                    return bet_amount * 100
            elif len(set(symbols)) == 2:
                return bet_amount * 5
            else:
                return -bet_amount