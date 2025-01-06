from app.users.auth import  Gestionnaireutilisateur
from app.interface.entrepassword import fenetre_conection,fenêtre_creation_compte
# pour l'instent code qui vat faire l'interaction entre l'utilisateur et les difféerent programe

gestionnaire = Gestionnaireutilisateur()
utilisateur_connecte = gestionnaire.utilisateur_connecte 

def main():
    menu_1()
    



def menu_1():  # Affichage d'un menu dans le terminal
    choix = False
    while True:
        print("1: Se connecter")
        print("2: Créer un utilisateur")
        print("3: Quit")
        choix_connections = int(input("Choisissez votre option : "))
        print("------------------------------------------")
        if choix_connections == 1:
            if fenetre_conection():
                menu_principal(gestionnaire)
        elif choix_connections == 2:
            if fenêtre_creation_compte() :
                menu_principal(gestionnaire)
        elif choix_connections == 3:
            print("fin de programme")
            break
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
            print("4: rechercher un Produit dans votre liste: ")
            print("5: retirer un produit : ")
            print("6: Se déconnecter")
            choix = int(input("Choisissez votre option : "))

            if choix == 1:
                gestionnaire.add_produit()
            elif choix == 2:
                gestionnaire.afficher_produits()
            elif choix == 3:
                gestionnaire.trie_utilisateur()
            elif choix == 4:
                gestionnaire.searche()
            elif choix == 5: 
                gestionnaire.deelet()
            elif choix == 6:
                gestionnaire.log_out()
                print("Vous êtes déconnecté.")
            else:
                print("Option invalide. Veuillez réessayer.")
    else:
        print("Vous n'êtes pas connecté.")
        



if __name__ == "__main__":
    main()
