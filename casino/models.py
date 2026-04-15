from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)  
    balance = models.IntegerField(default=1000)

class GameSession(models.Model):
    GAME_CHOICES = [
        ('blackjack', 'Blackjack'),
        ('roulette', 'Roulette'),
        ('slots', 'Slots'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=20, choices=GAME_CHOICES)
    bet_amount = models.IntegerField()
    result = models.CharField(max_length=10) #win or loss
    payout = models.IntegerField() #change in balance after game
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game} - {self.result} - {self.payout}"