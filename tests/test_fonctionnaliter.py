#test de la fonctionnaliter de tri avec une liste( est fonctionnelle plus que a modiffe avec les liste utilisateur)
import copy
import hashlib


def tri_rapide(liste):
    #Ont fait un tri qui vat choisire un pivot est trie par raport à celuis si en mettent dans une liste plus grand ou plus petite. 
    if liste != []:
        liste_plus_petite = []
        liste_plus_grande = []
        pivot = liste[0]
        for i in range(1,len(liste)):
            if liste[i] <= pivot:
                liste_plus_petite.append(liste[i])
            else:
                liste_plus_grande.append(liste[i])
        liste = tri_rapide(liste_plus_petite) + [pivot] +tri_rapide(liste_plus_grande)
    return liste 




#def searche_binaire(liste, nb_rechercher):
    debut= liste[0]
    fin=  len(liste) -1
    while debut <= fin:
        millieu = (debut + fin)//2
        if liste[millieu] == nb_rechercher:
            return millieu
        elif liste[millieu] < nb_rechercher:
            debut = millieu + 1 
        else:
           fin = millieu - 1 

#def searche_lineaire(liste, nb_recherche):
    if liste != []:
        for i in range(1,len(liste)-1):
            if liste [i] == nb_recherche:
                return i

#def delet_element(élement_chercher, liste):
    listecopy = copy.deepcopy(liste)
    tre = searche_lineaire(listecopy, élement_chercher)
    if tre != 1:
        liste.pop(tre) 
    return liste 


password ="test12"


def hash(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

password_hash = hash(password)

print(f"le mot de passe hasher {password_hash}")