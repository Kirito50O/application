import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fonction pour créer et afficher un diagramme en barres
def create_bar_chart():
    # Données pour le diagramme en barres
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [10, 20, 30, 40, 50]

    # Créer le diagramme en barres
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')

    # Ajouter des titres et labels
    ax.set_title('Diagramme en barres')
    ax.set_xlabel('Catégories')
    ax.set_ylabel('Valeurs')

    # Intégrer le diagramme dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # frame est le conteneur Tkinter pour le graphique
    canvas.draw()
    canvas.get_tk_widget().pack()

# Créer une fenêtre principale Tkinter
root = tk.Tk()
root.title("Diagramme en Barres avec Tkinter")

# Créer un conteneur pour le graphique
frame = ttk.Frame(root)
frame.pack()

# Créer un bouton pour afficher le diagramme
button = ttk.Button(root, text="Afficher le diagramme", command=create_bar_chart)
button.pack()

# Lancer l'interface Tkinter
root.mainloop()