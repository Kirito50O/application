from tkinter import *

window = Tk()

# personnaliser la fenétre 
window.title("mon application")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#c4bec7')

#crée la frame
frame = Frame(window, bg= "#c4bec7", bd=1, relief=SUNKEN)

#ajouter un texte
label_title = Label(frame, text="hello word", font=("Courrier, 30"), bg='#c4bec7', fg='black')
label_title.pack()

#ajouter un texte
label_subtitell = Label(frame, text="comment cela fonctionne", font=("Courrier, 15"), bg='#c4bec7', fg='black')
label_subtitell.pack(pady=25)

#metre un bouton
log_bouton = Button(frame, text="login", font=("Courrier, 15"), bg='black', fg='#c4bec7', command="fonction a appeller" )
log_bouton.pack()
#ajoute la boite 
frame.pack(expand=YES)
#afficher la fenétre
window.mainloop()