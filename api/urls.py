from django.urls import path
from .views import get_num_players, update_num_players
from .models import Game

game = None


def initialize_game():
    global game
    if game is None:
        # Create a new Game object if it doesn't exist
        game = Game.objects.create()


initialize_game()


urlpatterns = [
    # path('draw/', draw_card),
    # path('num-players/', get_num_players),
    # path('', index),
    path('update-num-players/', update_num_players),
    path('num-players/', get_num_players),

]
