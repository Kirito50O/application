# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
from app.fonctionaliter.produit_manager  import tri_rapide, searche_lineaire, searche_binaire, delet_element
from app.fonctionaliter.produit import Produit
from app.utils.security import verifiaction_api
import pandas as pd 
import hashlib




class Utilisateur:

    def  __init__(self, usr_name, password):
        self.usr_name = usr_name
        self.password_hash = password
        self.liste_produits = {}
        
    def __repr__(self):
        # Cette méthode permet d'afficher l'utilisateur de manière lisible
        return f"Utilisateur(username={self.usr_name}, password={self.password_hash})"

    def add_produit(self, produit):
        self.liste_produits[produit.name] = produit
    

    def verifications_password(self, password):
        password = password.strip()
        return self.password_hash == self.hash(password)
    
    # Ont hash pour le mettre dans la data base.
    def hash(self, password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        return sha256_hash.hexdigest()

    
#class fis qui vat appeller le parent Utisateur pour faire les actions  
class Gestionnaireutilisateur:

    def __init__(self):
        self.utilisatuers = {}
        self._utilisateur_connecte = None

    def hash(self, password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        return sha256_hash.hexdigest()

    def utilisateur_connecte(self):
        return self._utilisateur_connecte
    
    # Ont charge le ficher csv utilisateur dans le dictionnaire 
    def load_usr(self):
        df = pd.read_csv("data/users.csv")
        self.utilisatuers = {
            row['usr_name']: Utilisateur(row['usr_name'], row['password'])for _, row in df.iterrows()}
                

    
    # On charge le csv produit pour le mettre dans liste produit.
    def load_produit(self):
        df_produit = pd.read_csv("data/users_produits.csv")
        for _, row in df_produit.iterrows():
            usr_name = row["usr_name"]
            produit_name = row["produit"]
            produit_price = row["price"]
            produit_quantity = row["quantity"]
            produit= Produit(produit_name, produit_price, produit_quantity)
            if usr_name in self.utilisatuers:
                self.utilisatuers[usr_name].add_produit(produit)
            else:
                return f"Utilisateur {usr_name} non trouvé, pruduit non ajoutér"



    # On sauveguarde l'utilisateur dans le ficher csv utilisateur
    def save_usr(self):
        # Ajouter le nouvel utilisateur dans le DataFrame
        data = [(usr_name, utilisateur.password_hash) for usr_name, utilisateur in self.utilisatuers.items()]
        df_users = pd.DataFrame(data, columns=["usr_name", "password"])
        df_users.to_csv("data/users.csv", mode = 'a' ,header=False, index= False)
        

    # On sauveguarde les produit  dans le ficher csv users_produit
    def save_produit(self):
        data = []
        for usr_name, utilisateur in self.utilisatuers.items():
           for produit_name, produit in utilisateur.liste_produits.items():
               data.append([usr_name, produit.name, produit.price, produit.quantity])
        df_produit= pd.DataFrame(data ,columns =["usr_name" , "produit", "price", "quantity"])
        df_produit.to_csv("data/users_produits.csv",mode = 'a', header=False, index=False)


    

    #option pour crée un utilisateur
    def crée_utilisateur(self):
        usr_name = input("Entrée votre nom d'utilisateur : ")
        password = input("Entrée votre mots de passe : ").strip()
        if usr_name in self.utilisatuers:
            print ("Cette utilisateur existe déjà !!")
        else:
            if verifiaction_api(password):
                print("Votre mot de passe est compormit recommencer")
            else:
                password = self.hash(password)
                self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
                self._utilisateur_connecte = self.utilisatuers[usr_name]
                self.save_usr()
                print ("votre compte est crée !!")
                return True
        return None


    #option pour ce connectée 
    def login (self):
        self.load_usr()
        usr_name = input("Entrée votre nom d'utilisateur : ")
        password = input("Entrée votre mot de passe : ").strip()
        password_verifier = verifiaction_api(password)
        utilisateur = self.utilisatuers.get(usr_name)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!")
            
        elif utilisateur.verifications_password(password):
            self._utilisateur_connecte = utilisateur
            print("Vous êtes connecté")
            return True
        elif password_verifier:
            print("vous devais changer le mot de passe ")
            return True
        else:
            print ("Le mot de passe est incorrect")
        return None

    # Option pour ce déconnécté 
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
                self._utilisateur_connecte.liste_produits[produit.name] = produit
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
                    print(f"Produit trouvé : {self._utilisateur_connecte.liste_produits[index]}")
                else:
                    print("Produit non trouvé.")  
