#Import
from random import *
from structure import Player_file
from monitor.Init_game import *


class Card:
    # Init deck
    colors = ["Spade", "Club", "Heart", "Diamond"]
    values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Valet", "Dame", "Roi", "As"]

    def __init__(self, value, color):
        self.value = value
        self.color = color


class Deck:
    # construction du deck Yu! Gi! Oh!
    deck = [Card(value, color) for value in Card.values for color in Card.colors]

    # on shuffle les nombres et les couleurs du deck
    @classmethod
    def shuffle(cls):
        shuffle(Deck.deck)
        pass

    @classmethod
    def distribute(cls, nb_player):
        # Calling shuffle method ta vu
        Deck.shuffle()

        j = 0
        k = 0
        # Distribute randomly to players 2 cards, fait tapis mon pote
        for i in range(0, nb_player * 2, 1):
            # tirage de la carte mon frère (première carte du packet)
            card = Deck.deck[0]

            # distribution de la carte au joueur  (Il faut encore donner une valeur à la variable générale)
            Player_file.Player.player_hand(global_variable.liste_player[j], card, j, k)

            # on enlève la carte du paquet pour pouvoir mieux la remettre
            Deck.deck.remove(card)
            i += 1
            j += 1

            if j == nb_player:
                j = 0
                k = 1

    def distribute_table(self):
        # creating list
        list = []

        for i in range(0, self):
            # tirage de la première carte du packet
            card = Deck.deck[0]

            # appending instances to list
            list.append(Card(card.value, card.color))
            Deck.deck.remove(card)
            i += 1

        return list
