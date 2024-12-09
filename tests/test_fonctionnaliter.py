#test de la fonctionnaliter de tri avec une liste( est fonctionnelle plus que a modiffe avec les liste utilisateur)

liste = [ 5, 2, 8, 4, 6, 7, 1, 9, 3 ]

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


sorted_liste = tri_rapide(liste)

print(sorted_liste)
