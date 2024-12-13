# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
from app.fonctionaliter.produit_manager  import tri_rapide, searche_lineaire, searche_binaire, delet_element
from app.fonctionaliter.produit import Produit
import os

class Utilisateur:

    def  __init__(self, usr_name, password):
        self.usr_name = usr_name
        self.password = password
        self.liste_produits = []
        
    
    

    def verifications_password(self, password):
        return self.password == password
    
#class fis qui vat appeller le parent Utisateur pour faire les actions  
class Gestionnaireutilisateur:

    def __init__(self):
        self.utilisatuers = {}
        self._utilisateur_connecte = None 
        self.load_usr()

    def utilisateur_connecte(self):
        return self._utilisateur_connecte
    

    def load_usr(self):
        with open("data/users.txt","r") as file_user : 
            for line in file_user:
                usr_name, password = line.strip().split(':')
                self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
    
    def load_produit(self):
        with open("data/users_produit.txt", "r") as file_produits:
            current_usr = None
            for line in file_produits:
                line.strip()
                print(f"current_usr = {current_usr}") 
                if line.endswith(':'):
                    current_usr = line.rstrip(':')
                    print(f"current_usr = {current_usr}") #suprime les (":") pour simplifier le traitement du self.usrname
                if current_usr and current_usr in self.utilisatuers: #si il y a l'utilisatuer dans le dictionaire self.utilisateur
                    name,price,quantity = line.split(',')
                    produit= Produit(name, int(price), float(quantity)) # Ont crée  les instance de la class Produit
                    print(f"Produit ajouté pour {current_usr}: {produit.name}, {produit.price}, {produit.quantity}")
                    self.utilisatuers[current_usr].liste_produits.append(produit) # On met la liste de l'utilisateur dans la liste_produits  
                else :
                    print('void')
                    
    
    def save_usr(self):
        with open("data/users.txt","w")as file_user :
            for usr_name, utilisateur in self.utilisatuers.items():
                file_user.write(f"{usr_name}:{utilisateur.password}\n")

            
    def save_produit(self):
        with open("data/users_produit.txt","w") as file_produits:
            for usr_name, utilisateur in self.utilisatuers.items():
                file_produits.write(f"{usr_name}:")
                for produit in utilisateur.liste_produits:
                    file_produits.write(f" -{ produit.name}, {produit.price},{produit.quantity}")



            

    #option pour crée un utilisateur
    def crée_utilisateur(self):
        usr_name = input("Entrée votre nom d'utilisateur : ")
        password = input("Entrée votre mots de passe : ")
        if usr_name in self.utilisatuers:
            print ("Cette utilisateur existe déjà !!")
        else:
            self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
            self._utilisateur_connecte = self.utilisatuers[usr_name]
            self.save_usr()
            self.save_produit()
            print ("votre compte est crée !!")
            return True
        return None


    #option pour ce connectée 
    def login (self):
        usr_name = input("Entrée votre nom d'utilisateur : ")
        password = input("Entrée votre mot de passe : ")
        utilisateur = self.utilisatuers.get(usr_name)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!")
        elif utilisateur.verifications_password(password):
            self._utilisateur_connecte= utilisateur
            self.load_produit()
            print(f"Vous êtes connecté {usr_name}: votre liste de produit actuelle {self._utilisateur_connecte.liste_produits}" )
            
            return True
        else:
            print ("Le mot de passe est incorrect")
        return None
    
    def log_out(self):
        self._utilisateur_connecte = None
        print("utilisateur déconnéctér")



    #  affiche les different produit
    def afficher_produits(self):
        if self._utilisateur_connecte:
            self.load_produit()
            print(f"produit de {self._utilisateur_connecte.usr_name} : {self._utilisateur_connecte.liste_produits}")
        else:
            print("Aucun utilisateur connecté pour afficher une liste.")

    # Opptions de trie
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
            if self._utilisateur_connecte.liste_produits:
                self._utilisateur_connecte.liste_produits, key = tri_rapide(self._utilisateur_connecte.liste_produits, key)
                print(f"les produit sont trié {self._utilisateur_connecte.liste_produits}")
            else:
                print("votre liste et vide") 
    
    # Permet a l'utilisateur d'entrer ce que il veut ajouter 

    def add_produit(self):
        if self.utilisateur_connecte:
            choix = False
            while choix == False:
                name = input("Entre le nom du produits :")
                price = float(input("Entre le prix:"))
                quantity= int(input("Entrée la quantiter : "))
                produit = Produit(name, price, quantity)
                self._utilisateur_connecte.liste_produits.append(produit)
                self.save_produit()
                print(f"Le Produit '{produit.name}' à étais ajouter avec réusite !")
                break
        else:
            print("vous devais vous connecter !!!")
    
    #Permet a l'utilisateur de pouvoir mettre ce que l'utilisateur veut supprimer
    
    def deelet(self):
        if not self._utilisateur_connecte:
            print("Veuillez d'abord vous connecter.")
            return
        else:
            nom_produit = input("Entrez le nom du produit à supprimer : ")
            # Appel de la fonction de suppression
            self._utilisateur_connecte.liste_produits = delet_element(nom_produit, self._utilisateur_connecte.liste_produits)

    #Permet a l'utilisateur de pouvoir rechecher un élement

    def searche(self):
        if not self._utilisateur_connecte:
            print("vous étes pas connecter")
        else: 
            print("1 : recherche linéaire")
            print("2 : recherche binaire")
            choix_searche = int(input("Quelle type de recheche vouler vous faire :"))
            if choix_searche == 1:
                nom_produit = input("Entrez le nom du produit à rechercher (linéaire) : ")
                index = searche_lineaire(self._utilisateur_connecte.liste_produits, nom_produit)
                if index != -1:
                    print(f"Produit trouvé : {self._utilisateur_connecte.liste_produits[index].name}")
            elif choix_searche == 2: 
                nom_produit = input("Entrez le nom du produit à rechercher (binaire) : ")
                index = searche_binaire(self._utilisateur_connecte.liste_produits, nom_produit)
                if index != -1:
                    print(f"Produit trouvé : {self._utilisateur_connecte.liste_produits[index].name}")
                else:
                    print("Produit non trouvé.")  
