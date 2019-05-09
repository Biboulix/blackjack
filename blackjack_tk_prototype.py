from tkinter import *
from bibli import *
import random

#---------------------------------------------------------------------------#
#Fonctions
def image(sabot,nb_carte):
    if nb_carte <=6:
        coord_y = coord_y_joueur[0]
    else:
        coord_y = coord_y_joueur[1]

    carte = sabot * 4 - 1
    couleur = random.randint(0,3)
    carte_finale = carte - couleur
    img = PhotoImage(file=liste_carte[carte_finale])
    can.image= img
    can.create_image(coord_x[nb_carte-1],coord_y, image=img, anchor = NW)

#valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11

# Tirage des cartes
def sabot() :
    global nb_carte
    valeur = 0
    print("Total ", valeur)
    sabot = random.randint(0,13)
    nb_carte = nb_carte + 1

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

    elif sabot == 1 :                     #appelle la fonction as
        as_valeur = valeur_as()
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

    print("Vous avez un total de ", valeur)


#------------------------------------------------------------#
# Fenetre master

fen = Tk()
fen.title('BlackJack')

#--------------------------------------------------------------#
# Tapis vert #

can = Canvas(fen, width =1030, height =850, bg ='sea green')

logo = PhotoImage(file="logo.gif")
can.create_image(515,425, image=logo)

#--------------------------------------------------------------#
# Case blanches haut #

x1,y1,x2,y2 = 50,15,175,200
x3,y3,x4,y4 = 130,210,255,395
for f in range(0,6):
    can.create_rectangle(x1,y1,x2,y2,outline="snow")
    x1,x2 = x1+160, x2+160
for f in range(0,5):
    can.create_rectangle(x3,y3,x4,y4,outline="snow")
    x3,x4 = x3+160, x4+160

# Case blanches bas

x5,y5,x6,y6 = 130,455,255,640
x7,y7,x8,y8 = 50,650,175,835
for f in range(0,5):
    can.create_rectangle(x5,y5,x6,y6,outline="snow")
    x5,x6 = x5+160, x6+160
for f in range(0,6):
    can.create_rectangle(x7,y7,x8,y8,outline="snow")
    x7,x8 = x7+160, x8+160

#--------------------------------------------------------------#
# Test de posage de cartes

nb_carte = 0


#--------------------------------------------------------------#
# Bouton #

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').grid(row=0,column=1)
Button(fen,text='Carte',command=sabot, highlightbackground='#3E4149').grid(row=0,column=2)

#--------------------------------------------------------------#
# Initatilisation de fenetre master
can.grid(row=0,column=0)
fen.mainloop()
