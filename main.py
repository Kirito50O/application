from app.users.auth import  Gestionnaireutilisateur
# pour l'instent code qui vat faire l'interaction entre l'utilisateur et les difféerent programe
gestionnaire = Gestionnaireutilisateur()
def main():
    print(menu_1())


def menu_1 ():#affichage d'un menue dans le terminal 
    choix = False
    while choix == False:
        print("1: loging")
        print("2 : crée un utilisateur")
        choix_connections = int(input("Chaoisiser voutre options: "))
        print("------------------------------------------")
        if choix_connections == 1:
            print(login(gestionnaire))
            choix = True
        elif choix_connections == 2:
            print(crée_utilisateur(gestionnaire))
            choix = True
        elif choix_connections != 1 or choix_connections != 2:
            print("vous dever choisire entre le choix 1 ou 2 !! ")


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





