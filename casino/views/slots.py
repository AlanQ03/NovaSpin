from django.shortcuts import render
from casino.game_logic.slots import Slots
from casino.models import Users, GameSession

def play_slots(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':

        try:
            bet_amount = int(request.POST.get('bet_amount'))
        except (ValueError, TypeError):
            return render(request, 'casino/templates/pages/slots.html', {'error': 'Invalid bet amount'})
        
        if bet_amount <= 0 or bet_amount > user.balance:
            return render(request, 'casino/templates/pages/slots.html', {'error': 'Invalid bet amount'})
        
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

        return render(request, 'casino/templates/pages/slots.html', {
            'symbols': symbols,
            'payout': payout,
            'balance': user.balance
        })
    
    return render(request, 'casino/templates/pages/slots.html')