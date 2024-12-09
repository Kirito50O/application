# Pour l'instant ce fichier vat gére la création des utilisateur est les mettre plus tard dans une liste
# ont def ce que c'est un utilisateur
class Utilisateur:

    def  __int__(self, usr_name, password):
        self.usr_name = usr_name
        self.password = password
    
    def verifications_password(self, password):
        return self.password == password
    
#class fis qui vat appeller le parent Utisateur pour faire les actions  
class Gestionnaireutilisateur(Utilisateur) :
    def __init__(self, usr_name, password):
        super().__init__(usr_name, password)
        self.utilisatuers = {}
    
    #option pour crée un utilisateur
    def crée_utilisateur(self, usr_name, password):
        if usr_name in self.utilisatuers:
            print("Cette utilisateur existe déjà !!")
        else:
            self.utilisatuers[usr_name] = Utilisateur(usr_name, password)
            print("votre compte est crée !!")


    #option pour ce connectée 
    def login (self, usr_name, password):
        utilisateur = self.utilisatuers.get(usr_name)
        if usr_name:
            if utilisateur.verifications_password(password):
                return "vous éte connecté"
            else:
                return "le mot de passe est incorrecte"
        else:
            return f"l'utilisateur '{usr_name}' n'existe pas !!"
            


    