# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
from app.fonctionaliter.produit import *
from app.users.auth import *
from main import * 


# Options d'ajouter un produit (pas encore tester)
def add_produit(utilisateur_connecte):
    if utilisateur_connecte:
        name = input('Nom du produit:')
        price = float(input( "Prix du produit :"))
        quantity = int(input("Quantité du produit :"))
        produit = {"name" : name, "price" : price, "quantity" : quantity}
        utilisateur_connecte.liste_produits.append(produit)

#option de tris des produi( pour l'instent non mis car attend la fonction pour ce log)

def tri_rapide(liste,key):
    if liste != []:
        liste_plus_petit=[]
        liste_greadest=[]
        pivot = liste[0]
        for i in range (1 ,len(liste)):
            if liste[i][key] <= pivot[key]:
                liste_plus_petit.append(liste[i])
            else:
                liste_greadest.append(liste[i])
        liste = tri_rapide(liste_plus_petit, key)+ [pivot] +tri_rapide(liste_greadest, key)
    return liste


# fonction de recherche de un produit dans la liste
#def searche_binaire(liste, nb_rechercher):

    
#def searche_lineaire():
    