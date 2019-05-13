from tkinter import *
from bibli import *
import random
import sys
import os

#---------------------------------------------------------------------------#
#Fonctions
def return_un():
    return 1

def return_onze():
    return 11

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def valeur_as():
    valeur = valeur_as_string.get()
    return valeur

def image(sabot,nb_carte):
    if nb_carte <6:
        coord_y = coord_y_joueur[0]
    else:
        coord_y = coord_y_joueur[1]

    carte = (sabot-1) * 4
    couleur = random.randint(0,3)
    carte_finale = carte + couleur
    print(f"La carte est la carte {carte}, la couleur est {couleur} et la carte finale est donc {carte_finale}")
    img = PhotoImage(file=f"./cards/" + "card{}.gif".format(carte_finale))
    can.image= img
    can.create_image(coord_x[nb_carte],coord_y, image=img, anchor = NW)

# Tirage des cartes
def sabot() :
    global nb_carte
    global valeur
    sabot = random.randint(1,13)

    if sabot == 11 :
        print("valet")
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 12 :
        print("dame")
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 13 :
        print("roi")
        valeur = valeur + 10
        image(sabot,nb_carte)

    elif sabot == 1 :
        text_as = Label(fen, text="Quelle valeur de l'as voulez vous 1 ou 11 ?")
        text_as.grid(row = 0, column=1)
        valeur_as_string= StringVar()
        box = Entry(fen, textvariable=valeur_as_string)
        box.grid(row=0, column =2)
        Button(fen,text='Valide',command=valeur_as, highlightbackground='#3E4149').grid(row=1,column=1)

        if as_valeur == 1 :
            valeur = valeur + 1
            image(sabot,nb_carte)

        else:
            valeur = valeur + 11
            image(sabot,nb_carte)
    else :
        print(sabot)
        valeur = valeur + sabot
        image(sabot,nb_carte)
    nb_carte = nb_carte + 1

    nb_carte_string = StringVar()
    nb_carte_affichage = Label( fen, textvariable=nb_carte_string)

    nb_carte_string.set(f"Vous avez {nb_carte} cartes")
    nb_carte_affichage.grid(row=2)

    valeur_string = StringVar()
    valeur_affichage = Label( fen, textvariable=valeur_string)
    valeur_string.set(f"Vous avez {valeur} points")
    valeur_affichage.grid(row=2,column=1)


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


#--------------------------------------------------------------#
# Bouton #

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').grid(row=1,column=1)
Button(fen,text='Carte',command=sabot, highlightbackground='#3E4149').grid(row=1,column=2)
Button(fen,text='Recommencer',command=restart_program, highlightbackground='#3E4149').grid(row=1,column=3)

#--------------------------------------------------------------#
# Initatilisation de fenetre master
can.grid(row=1,column=0)
fen.mainloop()
