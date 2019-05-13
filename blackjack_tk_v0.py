from tkinter import *
from bibli import *
import random
import sys
import os

#---------------------------------------------------------------------------#
#Fonctions

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)


def image(sabot,nb_carte):
    global liste_carte_img
    carte = (sabot-1) * 4
    couleur = random.randint(0,3)
    carte_finale = carte + couleur
    img = PhotoImage(file=f"./cards/" + "card{}.gif".format(carte_finale))
    liste_carte_img.append(img)
    can.image= img
    can.create_image(coord_x[nb_carte],coord_y_joueur[0], image=img, anchor = NW)

# Tirage des cartes
def sabot() :
    global nb_carte
    global valeur

    sabot = random.randint(1,13)

    if sabot == 11 :
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 12 :
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 13 :
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 1 :
        as_valeur = int(input("Entrez valeur as : "))

        if as_valeur == 1 :
            valeur = valeur + 1
            image(sabot,nb_carte)

        else:
            valeur = valeur + 11
            image(sabot,nb_carte)



    else :
        valeur = valeur + sabot
        image(sabot,nb_carte)



    nb_carte = nb_carte + 1


    valeur_string = StringVar()
    valeur_affichage = Label( fen, textvariable=valeur_string)
    valeur_string.set(f"Vous avez {valeur} points")
    valeur_affichage.place(x = 448, y = 825)


#------------------------------------------------------------#
# Fenetre master

fen = Tk()
fen.title('BlackJack')

#--------------------------------------------------------------#
# Tapis vert #

can = Canvas(fen, width =1030, height =800, bg ='sea green')

logo = PhotoImage(file="logo.gif")
can.create_image(515,425, image=logo)

#--------------------------------------------------------------#
# Test de posage de cartes

nb_carte = 0
valeur = 0
liste_carte_img = []


#--------------------------------------------------------------#
# Bouton #

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').place(x = 1050, y = 30)
Button(fen,text='Carte',command=sabot, highlightbackground='#3E4149').place(x = 1050, y = 60)
Button(fen,text='Recommencer',command=restart_program, highlightbackground='#3E4149').place(x = 1050, y = 90)

#--------------------------------------------------------------#
# Initatilisation de fenetre master
can.place(x = 0, y = 20)
fen.mainloop()
