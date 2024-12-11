from app.users.auth import  Gestionnaireutilisateur
# pour l'instent code qui vat faire l'interaction entre l'utilisateur et les difféerent programe

gestionnaire = Gestionnaireutilisateur()
utilisateur_connecte = gestionnaire.utilisateur_connecte 

def main():
    menu_1()
    menu_principal(gestionnaire)



def menu_1():  # Affichage d'un menu dans le terminal
    choix = False
    while not choix:
        print("1: Se connecter")
        print("2: Créer un utilisateur")
        choix_connections = int(input("Choisissez votre option : "))
        print("------------------------------------------")
        if choix_connections == 1:
            login(gestionnaire)
            choix = True
        elif choix_connections == 2:
            crée_utilisateur(gestionnaire)
            choix = True
        else:
            print("Vous devez choisir entre le choix 1 ou 2 !!")

def menu_principal(gestionnaire):
    if utilisateur_connecte:
        choix = False
        while not choix:
            print("\n=== Menu principal ===")
            print("1: Ajouter un produit")
            print("2: Afficher les produits")
            print("3: Trier les produits")
            print("4: Se déconnecter")
            choix = int(input("Choisissez votre option : "))

            if choix == 1:
                gestionnaire.add_produit()
            elif choix == 2:
                gestionnaire.afficher_produits()
            elif choix == 3:
                gestionnaire.trie_utilisateur()
            elif choix == 4:
                gestionnaire.log_out()
                print("Vous êtes déconnecté.")
            else:
                print("Option invalide. Veuillez réessayer.")
    else:
        print("Vous n'êtes pas connecté.")
        

def crée_utilisateur(gestionnaire):
    usr_name = input("entrée votre nom utilisateur : ")
    password = input("Entre votre mot de passe : ")
    gestionnaire.crée_utilisateur(usr_name, password)

def login(gestionnaire):
    usr_name = input("Entré votre nom d'utilisateur : ")
    password = input("Entrer votre mot de passe : ")
    gestionnaire.login(usr_name, password)

if __name__ == "__main__":
    main()
