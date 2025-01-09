#création des produit que les utilisateur vont mettre .
#ajout du produit elle comptien le les paramettre du produit 

class Produit:
    """
    Classe qui vat deffinir ce que c'est un produit exactement.
    """

    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = float(price)
        self.quantity = int(quantity)
    
    def __repr__(self):
        return f"Produit : '{self.name}' Prix : '{self.price}' Quantiter : '{self.quantity}'"

  

    
