from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from .serializers import PlayerSerializer, CardSerializer, GameSerializer
from .models import Card, Player, Game
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json
import random
from django.contrib import messages
from django.http import HttpResponse


@api_view(['GET'])
def get_num_players(request):
    try:
        # Retrieve the num_players value from the Game object
        game = Game.objects.first()
        num_players = game.num_players
        #num_players +=20

        #num_players = 1

        # Return the num_players value in a JSON response
        return JsonResponse({'num_players': num_players})
    except Exception as e:
        print("false")


@api_view(['POST'])
def update_num_players(request):
    try:
        # Fetch the existing Game object or create a new one if it doesn't exist
        num_players = request.data.get('num_players')
        game = Game.objects.first()
        game.num_players -= num_players


        game.save()

        # Return a success response
        return JsonResponse({'success': True})
    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)


'''
@csrf_exempt
def index(request):
    if request.method == 'POST':
        num_players = int(request.POST.get('num_players', 0))
        players = list(range(1, num_players + 1))
        first_player = random.choice(players)
        print("ok")
        return JsonResponse({'first_player': first_player})

    return HttpResponse("API is working")

@api_view(['GET'])
def get_num_players(request):
    game = Game.objects.first()
    if game is not None:
        num_players = game.num_players
        print("nice work")
        return JsonResponse({'num_players': num_players})
    else:
        print("not bad")
        return JsonResponse({'error': 'Game object does not exist'})


@api_view(['GET'])
def get_num_players(request):
    game = Game.objects.first()  # Assuming you have a single game object
    if game:
        game.num_players += 1000  # Add 10 to the existing num_players value
        game.save()  # Save the updated game object

        serializer = GameSerializer(game)
        return Response(serializer.data)
    else:
        return Response({'message': 'No game object found.'}, status=status.HTTP_404_NOT_FOUND)
'''
'''
@api_view(['GET'])
def draw_card(request, game_id, player_id):
    game = get_object_or_404(Game, id=game_id)
    player = get_object_or_404(Player, id=player_id)

    # Check if the player has already drawn a card
    if player.has_drawn_card:
        # Return response indicating the player cannot draw another card
        return JsonResponse({'card': None, 'player_turn': False})

    card = game.deck_cards.first()
    player.hands.add(card)
    game.deck_cards.remove(card)
    game.save()

    # Set the player's "has_drawn_card" attribute to True
    player.has_drawn_card = True
    player.save()

    # Return the card data and player's turn information in the response
    card_data = {'color': card.color, 'value': card.value}
    return JsonResponse({'card': card_data, 'player_turn': True})'''
