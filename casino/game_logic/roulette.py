import random

class Roulette:
    def __init__(self):
        self.NUMBERS = [{'number': 0, 'color': 'green'}, {'number': 1, 'color': 'red'}, {'number': 2, 'color': 'black'}, {'number': 3, 'color': 'red'}, {'number': 4, 'color': 'black'}, {'number': 5, 'color': 'red'},
                        {'number': 6, 'color': 'black'}, {'number': 7, 'color': 'red'}, {'number': 8, 'color': 'black'}, {'number': 9, 'color': 'red'}, {'number': 10, 'color': 'black'},
                        {'number': 11, 'color': 'red'}, {'number': 12, 'color': 'black'}, {'number': 13, 'color': 'red'}, {'number': 14, 'color': 'black'}, {'number': 15, 'color': 'red'},
                        {'number': 16, 'color': 'black'}, {'number': 17, 'color': 'red'}, {'number': 18, 'color': 'black'}, {'number': 19, 'color': 'red'}, {'number': 20, 'color': 'black'},
                        {'number': 21, 'color': 'red'}, {'number': 22, 'color': 'black'}, {'number': 23, 'color': 'red'}, {'number': 24, 'color': 'black'}, {'number': 25, 'color': 'red'},
                        {'number': 26, 'color': 'black'}, {'number': 27, 'color': 'red'}, {'number': 28, 'color': 'black'}, {'number': 29, 'color': 'red'}, {'number': 30, 'color': 'black'},
                        {'number': 31, 'color': 'red'}, {'number': 32, 'color': 'black'}, {'number': 33, 'color': 'red'}, {'number': 34, 'color': 'black'}, {'number': 35, 'color': 'red'},
                        {'number': 36, 'color': 'black'}]
    def spin(self):
        return random.choice(self.NUMBERS)
    
    def calculate_payout(self, bet_type, bet_amount):
        if bet_type == 'number':
            return bet_amount * 35
        elif bet_type == 'other':
            return bet_amount * 2
            
            