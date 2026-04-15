from django.shortcuts import render
from casino.game_logic.blackjack import Blackjack
from casino.models import Users, GameSession


def play_blackjack(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/blackjack.html', {
            'error': 'You must be logged in to play.'
        })

    username = request.user.username

    try:
        user = Users.objects.get(name=username)
    except Users.DoesNotExist:
        return render(request, 'pages/blackjack.html', {
            'error': f'No casino user exists with username "{username}".'
        })

    # First page load
    if request.method == 'GET':
        # optional: clear any old round when page is refreshed
        request.session.pop('player_hand', None)
        request.session.pop('dealer_hand', None)
        request.session.pop('bet', None)

        return render(request, 'pages/blackjack.html', {
            'balance': user.balance
        })

    action = request.POST.get('action')
    result = None

    # START A BRAND NEW ROUND
    if action == 'deal':
        try:
            bet = int(request.POST.get('bet'))
        except (ValueError, TypeError):
            return render(request, 'pages/blackjack.html', {
                'error': 'Invalid bet amount',
                'balance': user.balance
            })

        if bet <= 0 or bet > user.balance:
            return render(request, 'pages/blackjack.html', {
                'error': 'Insufficient balance',
                'balance': user.balance
            })

        game = Blackjack()
        game.deal_initial_cards()

        # Save ONLY simple data
        request.session['player_hand'] = game.player_hand
        request.session['dealer_hand'] = game.dealer_hand
        request.session['bet'] = bet

        player_total = game.calculate_hand_value(game.player_hand)
        dealer_showing = game.dealer_hand[0]

        # immediate blackjack
        if player_total == 21:
            user.balance += int(bet * 1.5)
            user.save()
            result = 'win'

            GameSession.objects.create(
                user=request.user,
                game='blackjack',
                bet_amount=bet,
                result=result,
                payout=int(bet * 1.5)
            )

            request.session.pop('player_hand', None)
            request.session.pop('dealer_hand', None)
            request.session.pop('bet', None)

        return render(request, 'pages/blackjack.html', {
            'player_hand': player_total,
            'dealer_hand': dealer_showing,
            'balance': user.balance,
            'bet': bet,
            'result': result
        })

    # HIT OR STAND MUST USE AN EXISTING ROUND
    player_hand = request.session.get('player_hand')
    dealer_hand = request.session.get('dealer_hand')
    bet = request.session.get('bet')

    if not player_hand or not dealer_hand or bet is None:
        return render(request, 'pages/blackjack.html', {
            'error': 'No active game found. Click Deal first.',
            'balance': user.balance
        })

    game = Blackjack()
    game.player_hand = player_hand
    game.dealer_hand = dealer_hand
    # IMPORTANT: do NOT assign game.deck from session

    if action == 'hit':
        game.player_hit()
        player_total = game.calculate_hand_value(game.player_hand)
        dealer_showing = game.dealer_hand[0]

        # Save updated hands
        request.session['player_hand'] = game.player_hand
        request.session['dealer_hand'] = game.dealer_hand

        if player_total > 21:
            user.balance -= bet
            user.save()
            result = 'loss'

            GameSession.objects.create(
                user=request.user,
                game='blackjack',
                bet_amount=bet,
                result=result,
                payout=-bet
            )

            request.session.pop('player_hand', None)
            request.session.pop('dealer_hand', None)
            request.session.pop('bet', None)

        return render(request, 'pages/blackjack.html', {
            'player_hand': player_total,
            'dealer_hand': dealer_showing,
            'balance': user.balance,
            'bet': bet,
            'result': result
        })

    if action == 'stand':
        game.dealer_play()

        player_total = game.calculate_hand_value(game.player_hand)
        dealer_total = game.calculate_hand_value(game.dealer_hand)

        if dealer_total > 21 or player_total > dealer_total:
            user.balance += bet
            result = 'win'
        elif player_total < dealer_total:
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

        request.session.pop('player_hand', None)
        request.session.pop('dealer_hand', None)
        request.session.pop('bet', None)

        return render(request, 'pages/blackjack.html', {
            'player_hand': player_total,
            'dealer_hand': dealer_total,
            'balance': user.balance,
            'bet': bet,
            'result': result
        })

    return render(request, 'pages/blackjack.html', {
        'error': 'Invalid action.',
        'balance': user.balance
    })