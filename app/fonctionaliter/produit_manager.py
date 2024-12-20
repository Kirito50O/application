# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
import copy

#options d'ajouter un produit (pas encore tester)

#option de tris des produi( pour l'instent non mis car attend la fonction pour ce log)

def tri_rapide(self, produits, key):
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



                                       
    