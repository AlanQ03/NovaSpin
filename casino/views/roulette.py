from django.shortcuts import render
from game_logic.roulette import Roulette
from models import Users, GameSession

def play_roulette(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':
        
        try:
            bet_amount = int(request.POST.get('bet_amount'))
        except (ValueError, TypeError):
            return render(request, 'casino/templates/pages/roulette.html', {'error': 'Invalid bet amount'})
        
        choice = request.POST.get('choice')

        if bet_amount <= 0 or bet_amount > user.balance:
            return render(request, 'casino/templates/pages/roulette.html', {'error': 'Invalid bet amount'})
        game = Roulette()
        roll = game.spin()
        if choice == roll['number']:
            payout = game.calculate_payout('number', bet_amount)
        elif choice == roll['color']:
            payout = game.calculate_payout('other', bet_amount)
        elif choice in ['even', 'odd'] and roll['number'] != 0:
            if choice == 'even' and roll['number'] % 2 == 0:
                payout = game.calculate_payout('other', bet_amount)
            elif choice == 'odd' and roll['number'] % 2 != 0:
                payout = game.calculate_payout('other', bet_amount)
            else:
                payout = -bet_amount
        else:
            payout = -bet_amount

        user.balance += payout
        user.save()

        GameSession.objects.create(
            user=request.user,
            game='roulette',
            bet_amount=bet_amount,
            result='win' if payout > 0 else 'loss',
            payout=payout
        )

        return render(request, 'casino/templates/pages/roulette.html', {
            'roll': roll,
            'payout': payout,
            'balance': user.balance
        })

    return render(request, 'casino/templates/pages/roulette.html')
        

