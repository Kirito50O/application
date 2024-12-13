
# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
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
class Gestionnaireutilisateur :
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
            return f"Cet utilisateur '{usr_name}' n'existe pas !!"
        elif utilisateur and Utilisateur.verifications_password(password):
            self.utilisateur_connecte = utilisateur
            return "Vous êtes connecté"
        else:
            return "Le mot de passe est incorrect"

        
    def afficher_produits(self):
        if self.utilisateur_connecte:
            self.utilisateur_connecte.afficher_produit()
        else:
            print("Aucun utilisateur connecté pour afficher une liste.")


def test():
    gestionnaire = Gestionnaireutilisateur()
    print("\n=== Connexion d'Alice ===")
    print(gestionnaire.login("test", "password123"))
    print("\n=== Affichage des produits d'Alice ===")
    gestionnaire.afficher_produits()
test()

def utilisateur_connecte(self):
    "Menu quand l'utilisateur et connectée"
    if not self.utilisateur_connecte:
        print("Pas d'utilisateur connectée")

    print(f"Bienvenue,{self.utilisateur_connecte.usr_name}!")



    def crée_utilisateur(self, usr_name, password):
        if usr_name in self.utilisatuers:
            print ("Cette utilisateur existe déjà !!")
        else:
            self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
            self._utilisateur_connecte = self.utilisatuers[usr_name]
            print ("votre compte est crée !!")
            return True
        return None


    #option pour ce connectée 
    def login (self, usr_name, password):
        utilisateur = self.utilisatuers.get(usr_name)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!")
        elif utilisateur.verifications_password(password):
            self._utilisateur_connecte= utilisateur
            print("Vous êtes connecté")
            return True
        else:
            print ("Le mot de passe est incorrect")
        return None







def crée_utilisateur_main(gestionnaire):
    usr_name = input("entrée votre nom utilisateur : ")
    password = input("Entre votre mot de passe : ")
    return gestionnaire.crée_utilisateur(usr_name, password)

def login_main(gestionnaire):
    usr_name = input("Entré votre nom d'utilisateur : ")
    password = input("Entrer votre mot de passe : ")
    return gestionnaire.login(usr_name, password)





""""def save_produit(self):
    with open("data/users_produit.txt", "w") as file_produits:
        for usr_name, utilisateur in self.utilisatuers.items():
            # Crée une chaîne pour les produits, séparés par '; '
            produits_str = "; ".join(
                f"{produit.name}, {produit.price}, {produit.quantity}"
                for produit in utilisateur.liste_produits
            )
            # Écrire l'utilisateur et ses produits sur une seule ligne
            file_produits.write(f"{usr_name}: {produits_str}\n")
"""