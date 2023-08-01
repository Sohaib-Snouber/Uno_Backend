from django.db import models

# Create your models here.
COLORS = (
    ('Red', 'Red'),
    ('Green', 'Green'),
    ('Blue', 'Blue'),
    ('Yellow', 'Yellow'),
    ('Wild', 'Wild')
)
VALUES = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'),
          (8, '8'), (9, '9'), ('Skip', 'Skip'), ('Reverse', 'Reverse'), ('Draw2', 'Draw2'),
          ('Just', 'Just'), ('Draw4', 'Draw4'))


class Card(models.Model):  # The Card model represents a single Uno card. It has two fields, color and value.
    color = models.CharField(max_length=10, choices=COLORS)
    value = models.CharField(max_length=10, choices=VALUES)


class Game(models.Model):  # The Game model represents the game details that allow us to make more than a game on same
    # server with same program, but to do that, we need to add the Game class to both Player and Card as relationship  .
    host = models.CharField(max_length=255)
    game_code = models.CharField(max_length=8)
    num_players = models.IntegerField(default=10)
    num_computers = models.IntegerField(default=0)
    player_turn = models.IntegerField(null=True)
    play_direction = models.IntegerField(default=1)

    deck_cards = models.ForeignKey(Card, related_name='deck_games', on_delete=models.CASCADE, null=True)
    discards = models.ForeignKey(Card, related_name='discard_games', on_delete=models.CASCADE, null=True)


class Player(models.Model):  # The Player model represents a player's name, points and his cards(hands).
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    hands = models.ManyToManyField(Card, related_name='player_hand')


# ManyToManyField used to maintain multiple cards in a player's hands, deck_cards, and discards. If you intend to have
# only a single card for each player's hands, deck_cards, and discards, you can switch use ForeignKey instead.

# the Card model represents a single Uno card, the Player model represents a player
'''
In the provided code, the Game model is separated from the Player and Card model for better data organization.
and logical programming variables

when designing a database model using Django's ORM (Object-Relational Mapping), it is often beneficial to represent
relationships between entities using separate models and establish the relationships using foreignkey or ManyToMany. 
'''
