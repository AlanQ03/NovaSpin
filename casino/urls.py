from django.urls import path
from casino.views import home, blackjack, roulette, slots

urlpatterns = [
    path('', home.home, name='home'),
    path('blackjack/', blackjack.play_blackjack, name='blackjack'),
    path('roulette/', roulette.play_roulette, name='roulette'),
    path('slots/', slots.play_slots, name='slots'),
]