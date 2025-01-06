from tkinter import *
from app.users.auth import Gestionnaireutilisateur  # Importation du gestionnaire d'utilisateurs
gestionnaire = Gestionnaireutilisateur()  # Créer une instance du gestionnaire

#créations des page
def creation_window(page_titre, texte_titre,window_size):
    window = Tk()
    window.title(page_titre)
    window.geometry(window_size)
    window.config(background='#c4bec7')

    label_titre = Label(window, text=texte_titre, font=("Helvetica", 30), bg='#c4bec7', fg='black')
    label_titre.pack(side=TOP, pady=15)
    return window


#création de la page login ou création usr
def window_login_creat_usr(mode='connexion'):
    
    if mode == 'connexion':
        page_titre = "Connexion"
        texte_titre = "Se connecter"
        window_size= "720x520"
    elif mode == 'création':
        page_titre = "Création de compte"
        texte_titre = "Créer un compte"
        window_size= "720x520"

    window = creation_window(page_titre,texte_titre,window_size)
    frame = Frame(window, bg="#c4bec7")
    frame.pack()

    # Champ pour le nom d'utilisateur
    label_usr = Label(frame, text="Entrez votre nom d'utilisateur", font=("Helvetica", 15), bg='#c4bec7', fg='black')
    label_usr.pack(pady=20)

    label_usr_entry = Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    label_usr_entry.pack()

    # Champ pour le mot de passe
    label_password = Label(frame, text="Entrez votre mot de passe", font=("Helvetica", 15), bg='#c4bec7', fg='black')
    label_password.pack(pady=20)

    label_password_entry = Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black', show="x")
    label_password_entry.pack()

    label_email = Label(frame, text="Entrez votre mail ", font=("Helvetica", 15), bg='#c4bec7', fg='black')
    label_email.pack(pady=20)
    
    label_email_entry = Entry(frame, font=("Helvetica", 15), bg='#c4bec7', fg='black')
    label_email_entry.pack()

    def action():
        usr_name = label_usr_entry.get()
        password = label_password_entry.get()
        mail = label_email_entry.get() if mode == "création" else None
        if mode =='connection':
            if gestionnaire.login(usr_name, password,mail):
                print("Connexion réussie !")
                
            else:
                print("Identifiants incorrects. Essayez à nouveau.")
        elif mode == 'création':
            if gestionnaire.cree_utilisateur(usr_name,password,mail):
                print("Votre compte est crée bienvenus !!")
            else:
                print("Il y à us une erreur !!")
        window.quit()  # Fermer la fenêtre après l'action
        
        #bouton de connection et de création
    
    if mode == 'connexion':
        Bouton_action = Button(frame, text="Se connecter", font=("Helvetica", 15), bg='black', fg='#c4bec7', command=action)

    elif mode == "création":
        Bouton_action = Button(frame, text="Créer un compte", font=("Helvetica", 15), bg='black', fg='#c4bec7', command=action)
    
    Bouton_action.pack()

    # Lancer la fenêtre Tkinter
    window.mainloop()
    # Retourner True si l'utilisateur est connecté
    # Retourner True si l'utilisateur est connecté
    if gestionnaire.utilisateur_connecte():
        return True
    else:
        return False


def fenetre_conection():
    # Créer la fenêtre de connexion 
    window_login_creat_usr(mode="connexion")



def fenêtre_creation_compte():
    # Créer la fenêtre de création de compte 
    window_login_creat_usr(mode="création")

""""
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
    def action():
"""