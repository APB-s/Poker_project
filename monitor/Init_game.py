# import
import os

from Other import global_variable
from structure import hand_game, table
from structure.DeckCard import Deck


def init():
    # Rajouter le nombre de joueur au début de la partie
    # permet de lancer dans une invite de commande le serveur
    os.system("gnome-terminal -e 'bash -c \"cd /home/apb/PycharmProjects/Poker_project/comunication && python execute_srv.py; exec bash;\"'")

def tour():
    Deck.distribute(global_variable.nb_player)

    hand_game.Partie.attribution_BB(hand_game.Partie)
    hand_game.Partie.deroulement(hand_game.Partie)

    # Tirage du flop
    print('\nVoici le flop: ')
    table.tirage_flop()

    # Tirage du turn
    print('\nVoici le turn: ')
    table.tirage_turn()

    # Tirage de la river
    print('\nVoici la river: ')
    table.tirage_river()