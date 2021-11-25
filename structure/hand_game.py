import random
from Other import global_variable


def attribution_random_BB():
    liste_BB = []
    # attribution de la BB & SB
    liste_BB.append(random.randrange(0, global_variable.nb_player))
    if liste_BB[0] == global_variable.nb_player - 1:
        liste_BB.append(0)
    else:
        liste_BB.append(liste_BB[0] + 1)

    return liste_BB


class Partie():

    nombre_de_main = 0
    liste_BB = []
    BB_value = 10

    def attribution_BB(self):
        if Partie.nombre_de_main == 0:
            liste = attribution_random_BB()
            for i in liste:
                Partie.liste_BB.append(i)
        else:
            Partie.liste_BB[0] += 1
            if Partie.liste_BB[0] == global_variable.nb_player - 1:
                Partie.liste_BB[1] = 0
            else:
                Partie.liste_BB[1] += 1

    def deroulement(self):
        print(Partie.liste_BB)
        