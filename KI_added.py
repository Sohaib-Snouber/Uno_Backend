import random


class Card:  # defining the Card as object
    def __init__(self, color, value):
        self.color = color
        self.value = value


class Player:  # defining the Player as object
    def __init__(self, name, points, hand):
        self.name = name
        self.points = points
        self.hand = hand

# dividing our Game to smaller parts by making classes, each class refers to a part in the game


class Spieler:  # the Spieler part will handle all functions related to it
    def __init__(self):
        self.All = []
        self.building_players_as_objects()

    def building_players_as_objects(self):
        for a_player in range(num_players):
            print("when you want to play with computer or computer vs computer"
                  "you have to name the computer exactly as inside the "
                  "brackets (Computer) ")
            name = str(input("What is the player's {} name: ".format(a_player + 1)))

            while any(name == player_name.name for player_name in self.All) and name != "Computer":
                print("This name is reserved. Please choose a different name.")
                name = str(input("What is the player's {} name: ".format(a_player + 1)))

            points = 0
            hand = []
            self.All.append(Player(name, points, hand))


class KartenDeck:  # the KartenDeck part will handle all functions related to it
    def __init__(self):  # defining the needed list to store cards in it
        self.cards = []

    def build(self):  # building the card deck
        colors = ["Red", "Green", "Blue", "Yellow"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw2"]
        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))
                if value != 0:
                    self.cards.append(Card(color, value))
            self.cards.append(Card("Wild", "Just"))
            self.cards.append(Card("Wild", "Draw4"))

    def shuffle(self):  # shuffle cards randomly
        random.shuffle(self.cards)

    def draw_card(self):  # drawing a card for every time it being called
        return self.cards.pop(0)


class Regelmeister:  # the Regelmeister part will handle all functions related to it
    def __init__(self):  # initialize some variables with some values
        self.player_turn = None
        self.play_direction = 1

    def no_winner(self):  # this asks if any player won
        for each_player in range(num_players):
            for is_winner in Spieler.All:
                if is_winner.points >= 500:
                    return False
            return True

    def show_player_hand(self):  # this shows cards that the player has
        print("{}'s Turn".format(Spieler.All[self.player_turn - 1].name))
        print("Your Hand")
        print("------------------")
        count = 1
        for card in Spieler.All[self.player_turn - 1].hand:
            print("{}) {} {}".format(count, card.color, card.value))
            count += 1
        print("")

    def players_points_update(self):  # this will update points after each round
        for counting in Spieler.All:
            for card_value in counting.hand:
                value = card_value.value
                if value in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    Spieler.All[self.player_turn - 1].points = Spieler.All[self.player_turn - 1].points + value
                else:
                    Spieler.All[self.player_turn - 1].points = Spieler.All[self.player_turn - 1].points + 20

    def get_7_cards(self):  # this gives each player '7 cards' at the first of each round
        for seven_card in range(7):
            for giving_card in range(num_players):
                Spieler.All[giving_card].hand.append(KartenDeck.draw_card())  # Sieben Karten für jeden spieler geben

    def random_first_turn(self):  # this will randomly choose the first player each round
        self.player_turn = random.randint(1, num_players)  # 1 , 2 , 3 ... num_players

    def next_player(self):  # this gives who will play next and make some actions related to that
        if last_played_card is not None:
            if last_played_card.value == "Reverse":
                self.play_direction = self.play_direction * -1
            elif last_played_card.value == "Skip":
                self.player_turn += self.play_direction
                if self.player_turn > num_players:
                    self.player_turn = 1
                elif self.player_turn < 1:
                    self.player_turn = num_players
            elif last_played_card.value == "Draw2":
                player_draw = self.player_turn
                player_draw += self.play_direction
                if player_draw > num_players:
                    player_draw = 1
                elif player_draw < 1:
                    player_draw = num_players
                Regelmeister.get_cards(2, player_draw)
            elif last_played_card.value == "Draw4":
                player_draw = self.player_turn
                player_draw += self.play_direction
                if player_draw > num_players:
                    player_draw = 1
                elif player_draw < 1:
                    player_draw = num_players
                Regelmeister.get_cards(4, player_draw)
        self.player_turn += self.play_direction
        if self.player_turn > num_players:
            self.player_turn = 1
        elif self.player_turn < 1:
            self.player_turn = num_players

    def round_done(self):  # this gives if a player has no more cards in his hand
        for check_player_hand in Spieler.All:
            if len(check_player_hand.hand) == 0:
                print("round is finished, now the next round will begin ")
                return False
        return True

    def get_cards(self, number_of_cards, which_player):  # this will give definite number of cards to definite player
        for num_card in range(number_of_cards):
            Spieler.All[which_player - 1].hand.append(KartenDeck.draw_card())

    def card_throw_allowed(self):  # this checks if player's chosen card can be played or not
        p = 0
        ii = 0
        if Ablagestapel.discard[-1].color == "Wild":
            if card_chosen.color == "Wild" and card_chosen.value == Ablagestapel.discard[-1].value:
                return False
        if card_chosen.color == Ablagestapel.color_now or card_chosen.value == Ablagestapel.value_now:
            return False
        if card_chosen.color == 'Wild':
            while ii < len(Spieler.All[self.player_turn - 1].hand):
                for card in Spieler.All[self.player_turn - 1].hand:
                    if card.color == Ablagestapel.color_now or card.value == Ablagestapel.value_now:
                        p += 1
                ii += 1
            if p == 0:
                return False
            elif p != 0:
                return True
        return True


class Ablagestapel:  # the Ablagestapel part will handle all functions related to it
    def __init__(self):  # defining the discard list and some important variable
        self.discard = []
        self.color_now = None
        self.value_now = None

    def first_card(self):  # this will draw a card from deck at the beginning so players know which card to play
        self.discard = []
        self.discard.append(KartenDeck.draw_card())

    def played_card(self, card):  # when player played a card then this card come on top of discard
        self.discard.append(card)

    def playing_color(self):  # this will update the color for the next player to know what is the color now
        colors = ["Red", "Green", "Blue", "Yellow"]
        if Ablagestapel.discard[-1].color == "Wild":
            for color_choosing in range(4):
                print("{}) {}".format(color_choosing + 1, colors[color_choosing]))
            # here computer will choose the color according to the largest number of the chosen color in hand
            chosen_color = 1
            if Spieler.All[Regelmeister.player_turn - 1].name == "Computer":
                number_color_hand = {'Red': 0, 'Green': 0, 'Blue': 0, 'Yellow': 0}
                max_value = 0
                for counting_color in Spieler.All[Regelmeister.player_turn - 1].hand:
                    if counting_color.color in number_color_hand:
                        number_color_hand[counting_color.color] += 1
                for key, value in number_color_hand.items():
                    if value > max_value:
                        max_value = value
                        chosen_color = list(number_color_hand.keys()).index(key) + 1
            else:
                while True:
                    try:
                        chosen_color = int(input("what color would you like to choose :"))
                        if 1 <= chosen_color <= 4:
                            break
                        else:
                            print("please enter a number between 1-4, What color would you like to choose? ")
                    except ValueError:
                        print("please enter a number between 1-4, What color would you like to choose? ")
            self.color_now = colors[chosen_color - 1]
            print(self.color_now)
        else:
            self.color_now = Ablagestapel.discard[-1].color

    def playing_value(self):  # this will update the value for the next player to know what is the value now
        self.value_now = Ablagestapel.discard[-1].value


def number_of_players():  # knowing how many players are going to play
    while True:
        try:
            players_number = int(input("How many players are going to play? "))
            if 2 <= players_number <= 10:
                return players_number
            else:
                print("Invalid. Please enter a number between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


num_players = number_of_players()
Spieler = Spieler()
Regelmeister = Regelmeister()
KartenDeck = KartenDeck()
Ablagestapel = Ablagestapel()

while Regelmeister.no_winner():

    KartenDeck.build()
    KartenDeck.shuffle()

    deck_counter = len(KartenDeck.cards)
    # erste Spieler bestimmen
    Regelmeister.random_first_turn()
    for empty_hand in Spieler.All:
        empty_hand.hand = []
        print("{} hat {} points".format(empty_hand.name, empty_hand.points))
    Regelmeister.get_7_cards()

    Ablagestapel.first_card()

    while Ablagestapel.discard[-1].color == "Wild":
        Ablagestapel.first_card()

    Ablagestapel.playing_color()
    Ablagestapel.playing_value()

    x1 = 1
    x2 = 2

    while Regelmeister.round_done():
        last_played_card = None
        if len(KartenDeck.cards) < 5:
            KartenDeck.cards.append(Ablagestapel.discard[:-1])
            Ablagestapel.discard.remove(Ablagestapel.discard[:-1])
        print("Card on top of discard is :{} {}".format(Ablagestapel.discard[-1].color, Ablagestapel.discard[-1].value))
        Regelmeister.show_player_hand()
        # here our stupid logic computer player
        if Spieler.All[Regelmeister.player_turn - 1].name == "Computer":
            computer_found_card = False
            for computer_card in Spieler.All[Regelmeister.player_turn - 1].hand:
                card_chosen = computer_card
                if not Regelmeister.card_throw_allowed():
                    computer_found_card = True
                    print("Computer played {} {}".format(card_chosen.color, card_chosen.value))
                    Spieler.All[Regelmeister.player_turn - 1].hand.remove(card_chosen)
                    Ablagestapel.played_card(card_chosen)
                    last_played_card = card_chosen
                    Ablagestapel.playing_color()
                    Ablagestapel.playing_value()
                    break
            if not computer_found_card:
                print("Computer have drawn a card.")
                Regelmeister.get_cards(1, Regelmeister.player_turn)
                Regelmeister.show_player_hand()
                card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[-1]
                if not Regelmeister.card_throw_allowed():
                    print("Computer played {} {}".format(card_chosen.color, card_chosen.value))
                    Spieler.All[Regelmeister.player_turn - 1].hand.remove(card_chosen)
                    Ablagestapel.played_card(card_chosen)
                    last_played_card = card_chosen
                    Ablagestapel.playing_color()
                    Ablagestapel.playing_value()
            print("player's {} have ended his turn".format(Regelmeister.player_turn))
            Regelmeister.next_player()
        else:
            print("{}) Play a card or {}) Draw a card".format(x1, x2))
            while True:
                try:
                    answer1 = int(input(" what do you want to choose: playing or drawing a card : "))
                    if answer1 == 1 or answer1 == 2:
                        break
                    else:
                        print("Invalid. Please enter 1 or 2.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            if answer1 == 1:
                while True:
                    try:
                        number_chosen = int(input("Which card do you want to play? "))
                        if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                            break
                        else:
                            print("Invalid. Please enter correct number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                while Regelmeister.card_throw_allowed():
                    print("Not a valid card.")
                    Regelmeister.show_player_hand()
                    print("{}) Play a card or {}) Draw a card".format(x1, x2))
                    while True:
                        try:
                            answer2 = int(input(" what do you want to choose: playing or drawing a card : "))
                            if answer2 == 1 or answer2 == 2:
                                break
                            else:
                                print("Invalid. Please enter 1 or 2.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    if answer2 == 2:
                        print("You have drawn a card.")
                        Regelmeister.get_cards(1, Regelmeister.player_turn)
                        Regelmeister.show_player_hand()
                        print("{}) Play a card or {}) pass my turn".format(x1, x2))
                        while True:
                            try:
                                answer3 = int(input(" what do you want to choose: play or finish your turn : "))
                                if answer3 == 1 or 2:
                                    break
                                else:
                                    print("Invalid. Please enter 1 or 2.")
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        if answer3 == 2:
                            print("player's {} have ended his turn".format(Regelmeister.player_turn))
                        elif answer3 == 1:
                            while True:
                                try:
                                    number_chosen = int(input("Which card do you want to play? "))
                                    if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                                        break
                                    else:
                                        print("Invalid. Please enter correct number.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")
                            card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                            while Regelmeister.card_throw_allowed():
                                print("Not a valid card.")
                                Regelmeister.show_player_hand()
                                print("{}) Play a card or {}) finish my turn".format(x1, x2))
                                while True:
                                    try:
                                        answer4 = int(input("what do you want to choose: playing or finish my turn : "))
                                        if answer4 == 1 or answer4 == 2:
                                            break
                                        else:
                                            print("Invalid. Please enter 1 or 2.")
                                    except ValueError:
                                        print("Invalid input. Please enter a valid number.")
                                if answer4 == 2:
                                    break
                                elif answer4 == 1:
                                    while True:
                                        try:
                                            number_chosen = int(input("Which card do you want to play? "))
                                            if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                                                break
                                            else:
                                                print("Invalid. Please enter correct number.")
                                        except ValueError:
                                            print("Invalid input. Please enter a valid number.")
                                    card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                                    if not Regelmeister.card_throw_allowed():
                                        break
                                    else:
                                        continue
                            if answer3 == 1:
                                answer1 = 3
                                print("You played {} {}".format(card_chosen.color, card_chosen.value))
                                Spieler.All[Regelmeister.player_turn - 1].hand.pop(number_chosen - 1)
                                Ablagestapel.played_card(card_chosen)
                                last_played_card = card_chosen
                                Ablagestapel.playing_color()
                                Ablagestapel.playing_value()

                                Regelmeister.next_player()
                        break
                    elif answer2 == 1:
                        while True:
                            try:
                                number_chosen = int(input("Which card do you want to play? "))
                                if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                                    break
                                else:
                                    print("Invalid. Please enter correct number.")
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                        if not Regelmeister.card_throw_allowed():
                            break
                    else:
                        continue
                if answer1 == 1:
                    print("You played {} {}".format(card_chosen.color, card_chosen.value))
                    Spieler.All[Regelmeister.player_turn - 1].hand.pop(number_chosen - 1)
                    Ablagestapel.played_card(card_chosen)
                    last_played_card = card_chosen
                    Ablagestapel.playing_color()
                    Ablagestapel.playing_value()

                    Regelmeister.next_player()

            if answer1 == 2:
                print("You have drawn a card.")
                Regelmeister.get_cards(1, Regelmeister.player_turn)
                Regelmeister.show_player_hand()
                print("{}) Play a card or {}) pass my turn".format(x1, x2))
                while True:
                    try:
                        answer6 = int(input(" what do you want to choose: playing or finish my turn : "))
                        if answer6 == 1 or answer6 == 2:
                            break
                        else:
                            print("Invalid. Please enter 1 or 2.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                if answer6 == 2:
                    print("player's {} have ended his turn".format(Regelmeister.player_turn))

                    Regelmeister.next_player()
                elif answer6 == 1:
                    while True:
                        try:
                            number_chosen = int(input("Which card do you want to play? "))
                            if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                                break
                            else:
                                print("Invalid. Please enter correct number.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                    while Regelmeister.card_throw_allowed():
                        print("Not a valid card.")
                        Regelmeister.show_player_hand()
                        print("{}) Play a card or {}) pass my turn".format(x1, x2))
                        while True:
                            try:
                                answer7 = int(input(" what do you want to choose: playing or finish my turn : "))
                                if answer7 == 1 or answer7 == 2:
                                    break
                                else:
                                    print("Invalid. Please enter 1 or 2.")
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        if answer7 == 2:
                            break
                        elif answer7 == 1:
                            while True:
                                try:
                                    number_chosen = int(input("Which card do you want to play? "))
                                    if 1 <= number_chosen <= len(Spieler.All[Regelmeister.player_turn - 1].hand):
                                        break
                                    else:
                                        print("Invalid. Please enter correct number.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")
                            card_chosen = Spieler.All[Regelmeister.player_turn - 1].hand[number_chosen-1]
                            if not Regelmeister.card_throw_allowed():
                                break
                    if answer6 == 1:
                        print("You played {} {}".format(card_chosen.color, card_chosen.value))
                        Spieler.All[Regelmeister.player_turn - 1].hand.pop(number_chosen - 1)
                        Ablagestapel.played_card(card_chosen)
                    last_played_card = card_chosen
                    Ablagestapel.playing_color()
                    Ablagestapel.playing_value()

                    Regelmeister.next_player()
    Regelmeister.players_points_update()

for a_winner in range(num_players):
    if Spieler.All[a_winner].points >= 500:
        winner = a_winner
        print(Spieler.All[winner].name + ' is the winner')

print("Game Over")
