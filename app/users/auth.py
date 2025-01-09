# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
from app.fonctionaliter.produit_manager  import tri_rapide, searche_lineaire, searche_binaire, delet_element
from app.fonctionaliter.produit import Produit
from app.utils.security import verifiaction_api
import pandas as pd 
import hashlib




class Utilisateur:

    def  __init__(self, usr_name, password, mail):
        self.usr_name = usr_name
        self.password_hash = password
        self.mail = mail 
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
            row['usr_name']: Utilisateur(row['usr_name'], row['password'], row['mail'])for _, row in df.iterrows()}
                

    
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
                utilisateur = self.utilisatuers[usr_name]
                if produit_name not in utilisateur.liste_produits:  # On vérifie que le produit n'existe pas déjà
                    utilisateur.add_produit(produit)

                else:
                    return f"Utilisateur {usr_name} non trouvé, pruduit non ajoutér"



    # On sauveguarde l'utilisateur dans le ficher csv utilisateur
    def save_usr(self):
        # Ajouter le nouvel utilisateur dans le DataFrame
        data = [(usr_name, utilisateur.password_hash, utilisateur.mail) for usr_name, utilisateur in self.utilisatuers.items()]
        df_users = pd.DataFrame(data, columns=["usr_name", "password","mail"])
        df_users.to_csv("data/users.csv", mode = 'a' ,header=False, index= False)
        

    # On sauveguarde les produit  dans le ficher csv users_produit
    def save_produit(self):
        df_existing = pd.read_csv("data/users_produits.csv")
        data = []
        for usr_name, utilisateur in self.utilisatuers.items():
           for produit_name, produit in utilisateur.liste_produits.items():
               data.append([usr_name, produit.name, produit.price, produit.quantity])
        df_produit= pd.DataFrame(data ,columns =["usr_name" , "produit", "price", "quantity"])
        df_merged = pd.concat([df_existing, df_produit]).drop_duplicates(subset=["usr_name", "produit"], keep="last")
        df_merged.to_csv("data/users_produits.csv", index=False)


    

    #option pour crée un utilisateur
    def cree_utilisateur(self,usr_name,password,mail):
        
        if usr_name in self.utilisatuers:
            print ("Cette utilisateur existe déjà !!")
        else:
            if verifiaction_api(password, mail):
                print("Votre mot de passe est compormit recommencer")
            else:
                password = self.hash(password)
                self.utilisatuers[usr_name] = Utilisateur(usr_name, password, mail)
                self._utilisateur_connecte = self.utilisatuers[usr_name]
                self.save_usr()
                print ("votre compte est crée !!")
                return True
        return None


    #option pour ce connectée 
    def login (self, usr_name, password, mail):
        self.load_usr()
        utilisateur = self.utilisatuers.get(usr_name)
        mail_usr=self.utilisatuers.get(mail)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!") 
            return None  
        if not utilisateur.verifications_password(password):
            print ("Le mot de passe est incorrect")
            return None
        if mail_usr is None:
            print(f"Le mail '{mail_usr}' existe pas")
            return None
        else: 
            password_verifier = verifiaction_api(password,mail)
            if password_verifier: 
                print("vous devais changer le mot de passe ")
            self._utilisateur_connecte = utilisateur
            print("Vous êtes connecté")
        return True


    # Option pour ce déconnécté 
    def log_out(self):
        self._utilisateur_connecte = None
        print("utilisateur déconnéctér")


    #  affiche les different produit
    def afficher_produits(self):
        if self._utilisateur_connecte:
            self.load_produit()
            # Retourner la liste des produits sous forme de dictionnaire
            return self._utilisateur_connecte.liste_produits
        else:
            print("Aucun utilisateur connecté pour afficher une liste.")
            return {}

    # Opptions de trie
    def trie_utilisateur(self, key):
        self.load_produit()  # Recharger les produits si nécessaire
        if self._utilisateur_connecte:
            if self._utilisateur_connecte.liste_produits:
                print(f"Liste des produits avant tri : {self._utilisateur_connecte.liste_produits}")
                
                # Appeler tri_rapide et mettre à jour la liste des produits
                produits_triees = tri_rapide(self._utilisateur_connecte.liste_produits, key)
                print(f"Produits triés par  : {produits_triees}")
                return produits_triees
            else:
                print("Votre liste de produits est vide.")
        else:
            print("Aucun utilisateur connecté.")

    # Permet a l'utilisateur d'entrer ce que il veut ajouter 
    def add_produit(self, name, price, quantity):
        if self.utilisateur_connecte:
            if name in self._utilisateur_connecte.liste_produits: #vérifi si le produit et pas déja dans le csv 
            # Si le produit existe on met à jour sa quantité
                produit = self._utilisateur_connecte.liste_produits[name]
                produit.quantity += quantity  # rajoute la quantiter au produi si elle est modifier
                self.save_produit()
                return f"Le Produit '{produit.name}' à étais ajouter avec réusite !"
            
            else:
                produit = Produit(name, price, quantity)
                self._utilisateur_connecte.liste_produits[produit.name] = produit
                self.save_produit()
                return f"Le Produit '{produit.name}' à étais ajouter avec réusite !"
        else:
            return "vous devais vous connecter !!!"


    #Permet a l'utilisateur de pouvoir rechecher un élement
    def searche(self, name_produit):
        self.load_produit()
        if self._utilisateur_connecte:
            produits = self._utilisateur_connecte.liste_produits
            for produit in produits.values():
                if produit.name.lower() == name_produit.lower():  # Ignorer la casse dans la comparaison
                    return produit
            print(f"Produit '{name_produit}' non trouvé.")
            return None
        else:
            print("Aucun utilisateur connecté pour effectuer une recherche.")
            return None

    """def deelet(self, name_produit):
        if not self._utilisateur_connecte:
            print("Veuillez d'abord vous connecter.")
        else:
            produit_dealet = self.searche(name_produit)
            if produit_dealet :
                del  self._utilisateur_connecte.liste_produits[name_produit]
                self.save_produit()
                return f'Le produit : {name_produit} est supprimer'
            else: 
                return "le produit est pas trouver"""
                
    def deelet(self, name_produit):
        if not self._utilisateur_connecte:
            print("Veuillez d'abord vous connecter.")
            return
        
        # Recherche du produit à supprimer
        produit_a_supprimer = self.searche(name_produit)
        
        if produit_a_supprimer:
            # Supprimer le produit de la liste de l'utilisateur
            del self._utilisateur_connecte.liste_produits[name_produit]
            
            # Sauvegarder à nouveau les produits dans le fichier CSV
            self.save_produit()
            
            return f"Le produit '{name_produit}' a été supprimé avec succès."
        else:
            return f"Le produit '{name_produit}' n'a pas été trouvé."
            