from django.shortcuts import render
from casino.game_logic.slots import Slots
from casino.models import Users, GameSession

def play_slots(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/slots.html', {'error': 'You must be logged in to play.'})
    

    try:
        user, created = Users.objects.get_or_create(user=request.user)
    except Users.DoesNotExist:
        return render(request, 'pages/slots.html', {'error': f'No casino user exists with username "{request.user.username}".'})

    if request.method == 'GET':
        
        return render(request, 'pages/slots.html', {
            'balance': user.balance
        })
    
    action = request.POST.get('action')

    if action == 'spin':
        try:
            bet_amount = int(request.POST.get('bet_amount'))
        except (ValueError, TypeError):
            return render(request, 'pages/slots.html', {
                'error': 'Invalid bet amount',
                'balance': user.balance
            })
        
        if bet_amount <= 0 or bet_amount > user.balance:
            return render(request, 'pages/slots.html', {
                'error': 'Invalid bet amount',
                'balance': user.balance
            })
        
        game = Slots()
        symbols = game.spin()
        payout = game.calculate_payout(symbols, bet_amount)

        user.balance += payout
        user.save()

        GameSession.objects.create(
            user=request.user,
            game='slots',
            bet_amount=bet_amount,
            result='win' if payout > 0 else 'loss',
            payout=payout
        )

        return render(request, 'pages/slots.html', {
            'symbols': symbols,
            'payout': payout,
            'balance': user.balance
        })
    
    return render(request, 'pages/slots.html', {
        'error': 'Invalid action',
        'balance': user.balance
    })