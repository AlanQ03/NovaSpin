from django.shortcuts import render
from game_logic.blackjack import Blackjack
from models import Users

def play_blackjack(request):
    if request.method == 'POST':
        bet = int(request.POST.get('bet'))
        if bet > Users.objects.get(id=request.user.id).balance:
            return render(request, 'blackjack.html', {'error': 'Insufficient balance'})