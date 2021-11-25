from structure import DeckCard


# ce qui ce passe lors du flop
def tirage_flop():
    nb_card = 3
    # tirage de trois cartes qui constituent le flop
    liste_carte = DeckCard.Deck.distribute_table(nb_card)

    for obj in liste_carte:
        # on affiche les cartes du flop
        print(obj.color, obj.value)


# ce qui ce passe lors du turn
def tirage_turn():
    nb_card = 1
    # tirage de trois cartes qui constituent le flop
    liste_carte = DeckCard.Deck.distribute_table(nb_card)

    for obj in liste_carte:
        # on affiche les cartes du flop
        print(obj.color, obj.value)


# ce qui ce passe lors de la river
def tirage_river():
    nb_card = 1
    # tirage de trois cartes qui constituent le flop
    liste_carte = DeckCard.Deck.distribute_table(nb_card)

    for obj in liste_carte:
        # on affiche les cartes du flop
        print(obj.color, obj.value)

# pot à n'importe quel moment de la main
