from app.users.auth import *
# pour l'instent code qui vat faire l'interaction entre l'utilisateur et les difféerent programe
def main():
    gestionnaire = Gestionnaireutilisateur()
    #affichage d'un menue dans le terminal 
    print("-------------veiller vous connectée-----------------")
    print("1: loging")
    print("2 : crée un utilisateur")
    choix_connections = input("Chaoisiser voutre options: ")
    print("------------------------------------------")
    if choix_connections == 1:
        login(gestionnaire)
    elif choix_connections == 2:
        crée_utilisateur(gestionnaire)

def crée_utilisateur(gestionnaire):
    usr_name = input("entrée votre nom utilisateur : ")
    password = input("Entre votre mot de passe : ")
    gestionnaire.crée_utilisateur(usr_name, password)

def login(gestionnaire):
    usr_name = input("Entré votre nom d'utilisateur : ")
    password = input("Entrer votre mot de passe : ")
    utilisateur = gestionnaire.login(usr_name, password)

if __name__ == "__main__":
    main()





