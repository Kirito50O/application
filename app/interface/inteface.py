from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

# Premier menue 
def window_menu1():
    window_menu1 = creation_window("menu", "Choix de connexion","620x320") 
    frame = Frame(window_menu1, bg="#c4bec7")
    frame.pack()
    button_connexion = Button(frame, text="Login", font=("Helvetica", 15), bg='black', fg='#c4bec7', command=fenetre_conection)
    button_connexion.pack(pady=20)
    button_creat = Button(frame, text="Créer un compte", font=("Helvetica", 15), bg='black', fg='#c4bec7', command=fenêtre_creation_compte)
    button_creat.pack()
    window_menu1.mainloop()

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
        mail = label_email_entry.get() 
        if mode =='connexion':
            if gestionnaire.login(usr_name, password,mail):
                label_connection_return= Label(frame, text="Bienvenue", font=("Helvetica", 15), bg='#c4bec7', fg='green')
                label_connection_return.pack()
                menu_option()
    
            else:
                label_connection_return= Label(frame, text="Identifiants ou mot de passe incorrects. Essayez à nouveau.", font=("Helvetica", 15), bg='#c4bec7', fg='red')
                label_connection_return.pack()
            
        elif mode == 'création':
            if gestionnaire.cree_utilisateur(usr_name,password,mail):
                print("Votre compte est crée bienvenus !!")
                menu_option()
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
    window.destroy()




def fenetre_conection():
    # Créer la fenêtre de connexion 
    return window_login_creat_usr(mode="connexion")



def fenêtre_creation_compte():
    # Créer la fenêtre de création de compte 
    return window_login_creat_usr(mode="création")


# Création menu principale 
def menu_option():
    window_principal= creation_window("menu", "Bienvenue dans le menue", "1000x720")
    frame = Frame(window_principal, bg="#c4bec7")
    frame.pack()
    #Button selection options
    Button_ajouter_produit = Button(frame, text="Ajouter un produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_add_produit)
    Button_ajouter_produit.pack(pady=10)
    Button_print_liste = Button(frame, text="Afficher les produits", font=("Helvetica", 13),bg='black', fg='#c4bec7', command=menu_afficher)
    Button_print_liste.pack(pady=10)
    Button_trie = Button(frame, text="Trier les produits", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_trie)
    Button_trie.pack(pady=10)
    Button_searche = Button(frame, text="rechercher un Produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=widow_searche)
    Button_searche.pack(pady=10)
    Button_dealet = Button(frame, text="retirer un produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=window_dealet)
    Button_dealet.pack(pady=10)
    Button_comand = Button(frame, text="Afficher les states commande", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=graph_comand)
    Button_comand.pack(pady=10)

    def close_log_out():
        gestionnaire.log_out()
        window_principal.destroy()

    Button_log_out = Button(frame, text="Se déconnecter", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=close_log_out)
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

    def action():
        name = entry_name.get()
        price = entry_price.get()
        quantity = entry_quantity.get()
        gestionnaire.add_produit(name,price,quantity)
        label_produit = Label(frame, text=f"le Produit {name} à été ajouter", font=("Helvetica", 13), bg='#c4bec7', fg='green')
        label_produit.pack(pady=20)
        

    buton_add = Button(frame,text="Ajoutée le produit", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=action)
    buton_add.pack(pady=15)
    window_add.mainloop()


def menu_afficher ():
    window_afficher = creation_window("Produits", "Liste des Produits", "1000x720")
    frame = Frame(window_afficher, bg="#c4bec7")
    frame.pack()


    label_choix=Label(frame, text="Choisiser le mode d'affichage", font=("Helvetica", 16), bg='#c4bec7', fg='black')
    label_choix.pack(pady= 15)


    def menu_liste():
        window_liste= creation_window("Produits", "Liste des Produits", "1000x720")
        frame = Frame(window_liste, bg="#c4bec7")
        frame.pack()
        label_titre = Label(frame, text="Liste des Produits", font=("Helvetica", 16), bg='#c4bec7', fg='black')
        label_titre.pack(pady=20)
        produits = gestionnaire.afficher_produits()
        # Appeler la méthode afficher_produits et récupérer les produits

        if produits:
            for produit_name, produit_info in produits.items():
                produit_texte = f"Produit : {produit_info.name} | Prix : {produit_info.price} | Quantité : {produit_info.quantity}"
                label_produit = Label(frame, text= produit_texte, font=("Helvetica", 13), bg='#c4bec7', fg='black')
                label_produit.pack(pady=5)
        else:
            label_vide = Label(frame, text="Aucun produit disponible.", font=("Helvetica", 13), bg='#c4bec7', fg='black')
            label_vide.pack(pady=20)
        window_liste.mainloop()

    def graph():
        window_graph = creation_window("Graphique", "Graphique des Porduit", "1000x720")
        frame = Frame(window_graph, bg="#c4bec7")
        frame.pack()

        label_titre = Label(frame, text="Graphe de vos produits", font=("Helvetica", 16), bg='#c4bec7', fg='black')
        label_titre.pack(pady=20)
        produits = gestionnaire.afficher_produits()

        name = []
        quantity =[]

        for produit_name, produits_info in produits.items():
            name.append(produits_info.name)
            quantity.append(produits_info.quantity)

        fig, ax = plt.subplots()
        ax.bar(name, quantity, color="#c93bdb")
        ax.set_title('Diagrame des produit avec la quantiter')
        ax.set_xlabel('Produis')
        ax.set_ylabel('Quantiter')
        canvas = FigureCanvasTkAgg(fig,master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        window_graph.mainloop()

    button_choix_liste= Button(frame,text="Affiche en liste ", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=menu_liste)
    button_choix_liste.pack()

    button_choix_graph= Button(frame,text="Affiche en graphique", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=graph)
    button_choix_graph.pack(pady=15)

    window_afficher.mainloop()



               



# Menue de trie 
def menu_trie():
    window_trie = creation_window("Trie", "Appuier pour trié la liste", "1000x720")
    frame = Frame(window_trie, bg="#c4bec7")
    frame.pack()
    def trie_price():
        produits_triees = gestionnaire.trie_utilisateur("price")
    # Vérification et construction du texte à afficher
        if produits_triees:
            produit_texte = "\n".join([f"{produit.name} - Prix: {produit.price} - Quantité: {produit.quantity}" for produit in produits_triees.values()])
        else:
            produit_texte = "Il y à pas de produit"
        label_tri = Label(frame, text=produit_texte, font=("Helvetica", 13), bg='#c4bec7', fg='black')
        label_tri.pack(pady= 20)

    def trie_quantity():
        produits_triees= gestionnaire.trie_utilisateur("quantity") 
        if produits_triees:
            produit_texte = "\n".join([f"{produit.name} - Prix: {produit.price} - Quantité: {produit.quantity}" for produit in produits_triees.values()])
        else:
            produit_texte = "Il y à pas de produit"
        label_tri = Label(frame, text=produit_texte, font=("Helvetica", 13), bg='#c4bec7', fg='black')
        label_tri.pack(pady= 20)


    
    buttons_trie_price = Button(frame, text="Trier Mes produits par prix", font=("Helvetica", 13),bg='black', fg='#c4bec7', command=trie_price)
    buttons_trie_price.pack(pady=10)
    buttons_trie_quantity = Button(frame, text="Trier Mes produits par quantiter", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=trie_quantity)
    buttons_trie_quantity.pack(pady=10)
    
    window_trie.mainloop()



#menu de recherche et de supprétion 

def menu_searche_dealet_produit(mode1='searche'):

    if mode1 == 'searche':
        page_titre = "searche"
        texte_titre = "Rechercher un produit"
        window_size= "1000x720"
    elif mode1 == 'dealet':
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
        name_produit= entry_produit.get()
        if mode1 == "searche":
            if gestionnaire.searche(name_produit):
                produit_searche =gestionnaire.searche(name_produit)
                txt_produit = f"votre porduit {produit_searche.name} est dans la liste"
                label_searche = Label(frame, text=txt_produit, font=("Helvetica", 13), bg='#c4bec7', fg='green')
                label_searche.pack(pady= 20)
            else : 
                label_searche= Label(frame, text="Votre produit et pas dans la liste", font=("Helvetica", 13), bg='#c4bec7', fg='red')
                label_searche.pack(pady= 20)

        elif mode1 == "dealet":
            gestionnaire.deelet(name_produit)
            label_dealt = Label(frame, text="Votre produit est suprimer", font=("Helvetica", 13), bg='#c4bec7', fg='red')
            label_dealt.pack(pady= 20)
    
    button_validations =  Button(frame,text="Valider", font=("Helvetica", 13),bg='black', fg='#c4bec7',command=action)
    button_validations.pack(pady=20)
    window_searche_dealet.mainloop()

def widow_searche():
    return menu_searche_dealet_produit(mode1="searche")

def window_dealet():
    return menu_searche_dealet_produit(mode1="dealet")

def graph_comand():
    window_graph = creation_window("graphique ", "graphique","1000x720")
    frame = Frame(window_graph, bg="#c4bec7")
    frame.pack()
    name, quantites = gestionnaire.count_command()

    fig, ax = plt.subplots()
    ax.bar(name, quantites, color="#2e43e5")
    ax.set_title('Diagrame des produit avec la quantiter')
    ax.set_xlabel('Produis')
    ax.set_ylabel('Quantiter')
    canvas = FigureCanvasTkAgg(fig,master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    window_graph.mainloop()



