# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
import copy
from app.fonctionaliter.produit import Produit
#options d'ajouter un produit (pas encore tester)

#option de tris des produi( pour l'instent non mis car attend la fonction pour ce log)


"""def tri_rapide(liste, key):
    if liste != []:
        liste_plus_petit=[]
        liste_greadest=[]
        pivot = liste[0]
        for i in range (1 ,len(liste)):
            if getattr(liste[i], key) <= getattr(pivot, key):
                liste_plus_petit.append(liste[i], key)
            else:
                liste_greadest.append(liste[i],key)
        # Appel récursif sur les sous-listes
        liste = tri_rapide(liste_plus_petit, key) + [pivot] + tri_rapide(liste_greadest, key)
    return liste"""

def tri_rapide(produits, key):
    return dict(sorted(produits.items(), key=lambda item : getattr(item[1], key),reverse =False))


def searche_binaire(liste, nb_rechercher):
     # S'assurer que la liste est triée par nom
    liste_triee = sorted(liste, key=lambda produit: produit.name)
    debut = 0
    fin = len(liste_triee) - 1
    
    while debut <= fin:
        millieu = (debut + fin) // 2
        if liste_triee[millieu].name == nb_rechercher:
            return millieu  # Retourne l'index du produit
        elif liste_triee[millieu].name < nb_rechercher:
            debut = millieu + 1
        else:
            fin = millieu - 1
    return -1 

def searche_lineaire(liste, nb_recherche):
    for i in range(len(liste)):
        if liste[i].name == nb_recherche:  # Vérifie si le nom du produit correspond
            return i  # Retourne l'index du produit trouvé
    return -1


def delet_element(élement_chercher, liste):
    listecopy = copy.deepcopy(liste)
    tre = searche_lineaire(listecopy, élement_chercher)
    if tre != 1:
        liste.pop(tre) 
    return liste 



                                       
    