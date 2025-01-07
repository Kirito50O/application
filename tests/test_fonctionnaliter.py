#test de la fonctionnaliter de tri avec une liste( est fonctionnelle plus que a modiffe avec les liste utilisateur)
import copy
import hashlib


def tri_rapide(liste):
    #Ont fait un tri qui vat choisire un pivot est trie par raport à celuis si en mettent dans une liste plus grand ou plus petite. 
    if liste != []:
        liste_plus_petite = []
        liste_plus_grande = []
        pivot = liste[0]
        for i in range(1,len(liste)):
            if liste[i] <= pivot:
                liste_plus_petite.append(liste[i])
            else:
                liste_plus_grande.append(liste[i])
        liste = tri_rapide(liste_plus_petite) + [pivot] +tri_rapide(liste_plus_grande)
    return liste 




#def searche_binaire(liste, nb_rechercher):
    debut= liste[0]
    fin=  len(liste) -1
    while debut <= fin:
        millieu = (debut + fin)//2
        if liste[millieu] == nb_rechercher:
            return millieu
        elif liste[millieu] < nb_rechercher:
            debut = millieu + 1 
        else:
           fin = millieu - 1 

#def searche_lineaire(liste, nb_recherche):
    if liste != []:
        for i in range(1,len(liste)-1):
            if liste [i] == nb_recherche:
                return i

#def delet_element(élement_chercher, liste):
    listecopy = copy.deepcopy(liste)
    tre = searche_lineaire(listecopy, élement_chercher)
    if tre != 1:
        liste.pop(tre) 
    return liste 


"assword =utryryryuyitriteuk1222"
password = "uufghfugdshug14444"


def hash(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

password_hash = hash(password)

print(f"le mot de passe hasher {password_hash}")


"""def login (self):
    self.load_usr()
    usr_name = input("Entrée votre nom d'utilisateur : ")
     password = input("Entrée votre mot de passe : ")
    mail = input("entrée votre mail : ")
    password_verifier = verifiaction_api(password,mail)
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




#main
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
            if fenêtre_creation_compte():
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
        print("Vous n'êtes pas connecté.")"""