from Other import global_variable


class Player:
    # On crée une liste de mains de chaque joueur (liste de liste)
    list_all_hands = []
    for i in range(0, global_variable.nb_player):
        player_hands = [i, i]
        list_all_hands.append(player_hands)

    def __init__(self, numero_joueur, stack):
        self.numero_joueur = numero_joueur
        self.hand = [2]
        self.stack = stack

    def player_hand(self, card, numero_joueur, numero_card):
        Player.numero_joueur = numero_joueur
        Player.numero_card = numero_card

        #Player.list_all_hands[numero_joueur].remove(numero_joueur)
        Player.list_all_hands[numero_joueur].insert(numero_card, card)

    def show_hand(self):
        for card in Player.list_all_hands:
            for obj in card:
                print(obj.color, obj.value)

    def maj_stack_joueur(self, somme, numero_joueur):
        Player.stack = Player.stack + somme
        Player.numero_joueur = numero_joueur

    def stack_joueur(self, numero_joueur):
        Player.numero_joueur = numero_joueur
        print("la valeur du stack du joueur ", Player.numero_joueur, " est de ", Player.stack)
