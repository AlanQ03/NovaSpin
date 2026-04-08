from django.shortcuts import render
from game_logic.blackjack import Blackjack
from models import Users

def play_blackjack(request):
    if request.method == 'POST':
        bet = int(request.POST.get('bet'))
        if bet > Users.objects.get(id=request.user.id).balance:
            return render(request, 'blackjack.html', {'error': 'Insufficient balance'})
        else:
            game = Blackjack()
            game.deal_initial_cards()
            player_hand = game.calculate_hand_value(game.player_hand)
            dealer_hand = game.dealer_hand[0] # Show only one dealer card
            if player_hand == 21:
                Users.objects.filter(id=request.user.id).update(balance=Users.objects.get(id=request.user.id).balance + bet * 1.5)
                return render(request, 'casino/templates/pages/blackjack.html', {'message': 'Blackjack! You win!', 'player_hand': player_hand, 'dealer_hand': dealer_hand, 'balance': Users.objects.get(id=request.user.id).balance})
            elif player_hand < 21:
                input = request.POST.get('action')
                while input == 'hit':
                    game.player_hit()
                    player_hand = game.calculate_hand_value(game.player_hand)
                    if player_hand > 21:
                        Users.objects.filter(id=request.user.id).update(balance=Users.objects.get(id=request.user.id).balance - bet)
                        return render(request, 'casino/templates/pages/blackjack.html', {'message': 'Bust! You lose.', 'player_hand': player_hand, 'dealer_hand': dealer_hand, 'balance': Users.objects.get(id=request.user.id).balance})
                    input = request.POST.get('action')
                    game.dealer_play()
                    dealer_hand = game.calculate_hand_value(game.dealer_hand)
                    if dealer_hand > 21 or player_hand > dealer_hand:
                        Users.objects.filter(id=request.user.id).update(balance=Users.objects.get(id=request.user.id).balance + bet)
                        return render(request, 'casino/templates/pages/blackjack.html', {'message': 'You win!', 'player_hand': player_hand, 'dealer_hand': dealer_hand, 'balance': Users.objects.get(id=request.user.id).balance})
                    elif player_hand < dealer_hand:
                        Users.objects.filter(id=request.user.id).update(balance=Users.objects.get(id=request.user.id).balance - bet)
                        return render(request, 'casino/templates/pages/blackjack.html', {'message': 'You lose.', 'player_hand': player_hand, 'dealer_hand': dealer_hand, 'balance': Users.objects.get(id=request.user.id).balance})
                    else:
                        return render(request, 'casino/templates/pages/blackjack.html', {'message': 'Push!', 'player_hand': player_hand, 'dealer_hand': dealer_hand, 'balance': Users.objects.get(id=request.user.id).balance})