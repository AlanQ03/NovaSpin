from django.shortcuts import render
from game_logic.blackjack import Blackjack
from models import Users, GameSession

def play_blackjack(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':
        bet = int(request.POST.get('bet'))

        if bet > user.balance:
            return render(request, 'casino/templates/pages/blackjack.html', {'error': 'Insufficient balance'})

        game = Blackjack()
        game.deal_initial_cards()

        player_hand = game.calculate_hand_value(game.player_hand)
        dealer_hand = game.dealer_hand[0]

        if player_hand == 21:
            user.balance += int(bet * 1.5)
            result = 'win'

        else:
            action = request.POST.get('action')

            if action == 'hit':
                game.player_hit()
                player_hand = game.calculate_hand_value(game.player_hand)

                if player_hand > 21:
                    user.balance -= bet
                    result = 'loss'
                else:
                    return render(request, 'casino/templates/pages/blackjack.html', {
                        'player_hand': player_hand,
                        'dealer_hand': dealer_hand
                    })

            elif action == 'stand':
                game.dealer_play()
                dealer_hand = game.calculate_hand_value(game.dealer_hand)

                if dealer_hand > 21 or player_hand > dealer_hand:
                    user.balance += bet
                    result = 'win'
                elif player_hand < dealer_hand:
                    user.balance -= bet
                    result = 'loss'
                else:
                    result = 'push'

        user.save()

        GameSession.objects.create(
            user=request.user,
            game='blackjack',
            bet_amount=bet,
            result=result,
            payout=bet if result == 'win' else -bet if result == 'loss' else 0
        )

        return render(request, 'casino/templates/pages/blackjack.html', {
            'result': result,
            'player_hand': player_hand,
            'dealer_hand': dealer_hand,
            'balance': user.balance
        })

    return render(request, 'casino/templates/pages/blackjack.html')