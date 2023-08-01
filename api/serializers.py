from rest_framework import serializers
from .models import Card, Player, Game


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'color', 'value')


class PlayerSerializer(serializers.ModelSerializer):
    hands = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'points', 'hands')


class GameSerializer(serializers.ModelSerializer):
    deck_cards = CardSerializer(many=True)
    discards = CardSerializer(many=True)
    '''host = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        allow_null=True,  # make the 'host' field optional
        required=False
    )'''
    game_code = serializers.CharField(read_only=True)
    host = serializers.CharField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'host', 'game_code', 'num_players', 'num_computers', 'player_turn', 'play_direction',
                  'deck_cards', 'discards')


# see how we use the serializers and see if I should name my serializers classes to some specific
# JavaScripts components or not
