from django.urls import path
from casino.views import home

urlpatterns = [
    path('', home.home, name='home'),
]