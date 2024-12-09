# programe de fonctionnaliter du site tout ce qui vat étre de toucher au produit qui existe. 
from fonctionaliter.produit import Produit

def add_produit():
    name = input('Nom du produit:')
    price = float(input( "Prix du produit :"))
    quantity = int(input("Quantité du produit :"))

    produit = Produit(name,price,quantity)
    produits = []
    produits.append(produit)
    print(f"produit'{name}' et ajouter.")

