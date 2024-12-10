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