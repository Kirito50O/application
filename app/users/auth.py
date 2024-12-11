# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
from app.fonctionaliter.produit_manager  import * 

class Utilisateur:

    def  __init__(self, usr_name, password):
        self.usr_name = usr_name
        self.password = password
        self.liste_produits = []
        
    
    
    def afficher_produit(self):
        print(f"Liste de produit de {self.usr_name} : {self.liste_produits}")

    def verifications_password(self, password):
        return self.password == password
    
#class fis qui vat appeller le parent Utisateur pour faire les actions  
class Gestionnaireutilisateur:

    def __init__(self):
        self.utilisatuers = {}
        self.utilisateur_connecte = None 

            

    #option pour crée un utilisateur
    def crée_utilisateur(self, usr_name, password):
        if usr_name in self.utilisatuers:
            print ("Cette utilisateur existe déjà !!")
        else:
            self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
            print ("votre compte est crée !!")


    #option pour ce connectée 
    def login (self, usr_name, password):
        utilisateur = self.utilisatuers.get(usr_name)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!")
        elif utilisateur.verifications_password(password):
            self.utilisateur_connecte = utilisateur
            print("Vous êtes connecté")
        else:
            print ("Le mot de passe est incorrect")

        
    def afficher_produits(self):
        if self.utilisateur_connecte:
            self.utilisateur_connecte.afficher_produit()
        else:
            print("Aucun utilisateur connecté pour afficher une liste.")

    def utilisateur_connecte(self):
        "Menu quand l'utilisateur et connectée"
        if not self.utilisateur_connecte:
            print("Pas d'utilisateur connectée")

        print(f"Bienvenue,{self.utilisateur_connecte.usr_name}!")
    
    def trie_utilisateur(self):
        if self.utilisateur_connecte:
            choix = False
            while choix == False:
                print("-------- Option de trie --------- ")
                print("1: trie par prix ")
                print("2 : trier par quantiter")
                choix_tri = int(input("faite votre choix :"))
                if choix_tri == 1 :
                    key = "price"
                    choix = True
                elif choix_tri == 2 :
                    key ="quantity"
                    choix = True
                else:
                    print("le choix existe pas")
            if not self.utilisateur_connecte.liste_produits:
                self.utilisateur_connecte.liste_produits, key = tri_rapide(self.utilisateur_connecte.liste_produits, key)
                print(f'les produit sont trié')
            else:
                print("votre liste et vide") 

