# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
from app.fonctionaliter.produit import *
from app.users.auth import *
import copy



# Options d'ajouter un produit (pas encore tester)
def add_produit(utilisateur_connecte):
    if utilisateur_connecte:
        name = input('Nom du produit:')
        price = float(input( "Prix du produit :"))
        quantity = int(input("Quantité du produit :"))
        produit = {"name" : name, "price" : price, "quantity" : quantity}
        utilisateur_connecte.liste_produits.append(produit)

#option de tris des produi( pour l'instent non mis car attend la fonction pour ce log)
def delet_element(élement_chercher, liste):
    listecopy = copy.deepcopy(liste)
    tre = searche_lineaire(listecopy, élement_chercher)
    if tre != 1:
        liste.pop(tre) 
    return liste 

def tri_rapide(liste_produits,key):
    if liste_produits != []:
        liste_plus_petit=[]
        liste_greadest=[]
        pivot = liste_produits[0]
        for i in range (1 ,len(liste_produits)):
            if liste_produits[i][key] <= pivot[key]:
                liste_plus_petit.append(liste_produits[i])
            else:
                liste_greadest.append(liste_produits[i])
        liste_produits = tri_rapide(liste_plus_petit, key)+ [pivot] +tri_rapide(liste_greadest, key)
    return liste_produits


def tri_bulle(liste):
    if liste == []:
        return False
    else:
        prmu = 1 
    
        while prmu != 0:  
            prmu = 0
            for i in range(len(liste)-1): 
                if liste[i] > liste[i+1]:
                    liste[i],liste[i+1] = liste[i+1],liste[i]
                    prmu += 1
        return liste



# fonction de recherche de un produit dans la liste
def searche_binaire(liste, nb_rechercher):
    debut= liste[0]
    fin=  len(liste) -1
    while debut <= fin:
        millieu = (debut + fin)//2
        if liste[millieu] == nb_rechercher:
            return millieu
        elif liste[millieu] < nb_rechercher:
            debut = millieu + 1 
        else:
           debut = millieu - 1 



def searche_lineaire(liste, nb_recherche):
    if liste != []:
        for i in range(1,len(liste)):
            if liste [i] == nb_recherche:
                return i
            

    