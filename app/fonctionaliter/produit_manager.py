# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
from fonctionaliter.produit import Produit

#options d'ajouter un produit (pas encore tester)
def add_produit():
    name = input('Nom du produit:')
    price = float(input( "Prix du produit :"))
    quantity = int(input("Quantité du produit :"))

    produit = Produit(name,price,quantity)
    produits = []
    produits.append(produit)
    print(f"produit'{name}' et ajouter.")

#option de tris des produi( pour l'instent non mis car attend la fonction pour ce log)

def tri_rapide(liste):
    if liste != []:
        liste_plus_petit=[]
        liste_greadest=[]
        pivot = liste[0]
        for i in range (1 ,len(liste)):
            if liste[i] <= pivot:
                liste_plus_petit.append(liste[i])
            else:
                liste_greadest.append(liste[i])
        liste = tri_rapide(liste_plus_petit)+ [pivot] +tri_rapide(liste_greadest)
    return liste


# fonction de recherche de un produit dans la liste
def searche():
    