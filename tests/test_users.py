
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



def crée_utilisateur(self):
    usr_name = input("Entrée votre nom d'utilisateur : ")
    password = input("Entrée votre mots de passe : ")
    if usr_name in self.utilisatuers:
        print ("Cette utilisateur existe déjà !!")
    else:
        new_usr = Utilisateur(usr_name,password)
        self.utilisateurs[usr_name] = new_usr
        self.utilisateur_connecte = new_usr
        print ("votre compte est crée !!")
        return True
    return None


  def login (self):
        self.load_usr()
        usr_name = input("Entrée votre nom d'utilisateur : ")
        password = input("Entrée votre mot de passe : ")
        mail = input("entrée votre mail : ")
        utilisateur = self.utilisatuers.get(usr_name)
        if utilisateur is None:
            print( f"Cet utilisateur '{usr_name}' n'existe pas !!")   
        if not utilisateur.verifications_password(password):
            print ("Le mot de passe est incorrect")
            return None
        else: 
            password_verifier = verifiaction_api(password,mail)
            if password_verifier: 
                print("vous devais changer le mot de passe ")
            self._utilisateur_connecte = utilisateur
            print("Vous êtes connecté")
        return True






    if gestionnaire.utilisateur_connecte():
        return True
    else:
        return False












def first_menu():
    window_first = creation_window()

# Création menu principale 
def menu_option():
    window_principal= creation_window("menu", "Bienvenue dans le menue", "1000x720")
    frame = Frame(window_principal, bg="#c4bec7")
    frame.pack()
    #Button selection options
    Button_ajouter_produit = Button(frame, text="Ajouter un produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_add_produit())
    Button_ajouter_produit.pack(pady=10)
    Button_print_liste = Button(frame, text="Afficher les produits", font=("Helvetica", 13),bg='black', fg='#c4bec7')
    Button_print_liste.pack(pady=10)
    Button_trie = Button(frame, text="Trier les produits", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_trie)
    Button_trie.pack(pady=10)
    Button_searche = Button(frame, text="rechercher un Produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_searche_dealet_produit(mode='searche'))
    Button_searche.pack(pady=10)
    Button_dealet = Button(frame, text="retirer un produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_searche_dealet_produit(mode='dealet'))
    Button_dealet.pack(pady=10)
    Button_log_out = Button(frame, text="Se déconnecter", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=gestionnaire.log_out())
    Button_log_out.pack(pady=10)

#menu ajouter produit 
def menu_add_produit():
    window_add = creation_window("add", "Ajoutée un Produit", "1000x720")
    frame = Frame(window_add, bg="#c4bec7")
    frame.pack()

    label_name = Label(frame, text="Entrez le nom du produit", font=("Helvetica", 13), bg='#c4bec7', fg='black')
    label_name.pack(pady=20)

    entry_name =  Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    entry_name.pack()

    label_price = Label(frame, text="Entrez le prix", font=("Helvetica", 13), bg='#c4bec7', fg='black')
    label_price.pack(pady=20)

    entry_price =Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    entry_price.pack()
    label_quantity = Label(frame, text="Entrez la quantiter", font=("Helvetica", 13), bg='#c4bec7', fg='black')
    label_quantity.pack(pady=20)

    entry_quantity = Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    entry_quantity.pack()


#def menu_afficher ():
# Menue de trie 
def menu_trie():
    window_trie = creation_window("Trie", "Appuier pour trié la liste", "1000x720")
    frame = Frame(window_trie, bg="#c4bec7")
    frame.pack()

    buttons_trie = Button(frame, text="Trier Mes produits", font=("Helvetica", 13),bg='black', fg='#c4bec7')

#menu de recherche et de supprétion 
def menu_searche_dealet_produit(mode='searche'):

    if mode == 'searche':
        page_titre = "searche"
        texte_titre = "Rechercher un produit"
        window_size= "1000x720"
    elif mode == 'dealet':
        page_titre = "dealet"
        texte_titre = "Supprimer un produit"
        window_size= "1000x720"

    window_searche_dealet= creation_window("searche", "Rechercher un produit","1000x720")
    frame = Frame(window_searche_dealet, bg="#c4bec7")
    frame.pack()

    label_produit = Label(frame, text="Entrez le nom du produit", font=("Helvetica", 13), bg='#c4bec7', fg='black')
    label_produit.pack(pady=20)

    entry_produit = Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    entry_produit.pack()
    #def action():
        

    if gestionnaire.utilisateur_connecte():
        return True
    else:
        return False
    

  def afficher_produits(self):
        if self._utilisateur_connecte:
            self.load_produit()
            print(f"produit de {self._utilisateur_connecte.usr_name} : {self._utilisateur_connecte.liste_produits}")
        else:
            print("Aucun utilisateur connecté pour afficher une liste.")

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

    def add_produit(self, name, price, quantity):
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