from tkinter import *
from bibli import *
import random
import sys
import os
import pickle

#---------------------------------------------------------------------------#
#Fonctions
def compte_joueur() :
	with open("donnees", "rb") as fichier :
		mon_depickler = pickle.Unpickler(fichier)
		mon_dico_joueur = mon_depickler.load()

		mon_pseudo = input("Veuillez entrer votre pseudo : \n ")
		if mon_pseudo in mon_dico_joueur.keys() :
			mon_score = mon_dico_joueur[mon_pseudo]
		else :
			mon_dico_joueur[mon_pseudo] = 500

	print("vous possédez actuellement",mon_dico_joueur[mon_pseudo]," $")
	mise = int(input("combien voulez vous misez ?"))
	while mise > compte_courant :
		print("vous ne pouvez pas miser plus que vous ne possédez !")
		mise = int(input("Donc combien voulez vous vraiment miser ?"))
		return mise
	compte_courant == compte_courant - mise
	return compte_courant


#Recommencer le programe
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

#--------------------------------------------------------------#



#Valeur de l'as

#Affichage des cartes
def image(sabot,nb_carte,coord_y):
    global liste_carte_img
    carte = (sabot-1) * 4
    couleur = random.randint(0,3)
    carte_finale = carte + couleur
    img = PhotoImage(file=f"./cards/" + "card{}.gif".format(carte_finale))
    liste_carte_img.append(img)
    can.image= img
    can.create_image(coord_x[nb_carte],coord_y, image=img, anchor = NW)


#Tirage des cartes
def sabot() :
	global nb_carte
	global valeur
	global valeur_string
	global coord_y_joueur
	coord_y = coord_y_joueur[0]
	sabot = random.randint(1,13)

	if valeur >21:
		perdu = "Vous avez perdu"
		label = Label( fen, text = perdu )

		label.place(x = 1040, y = 425,anchor = W)

	elif sabot == 11 :
		valeur = valeur + 10
		image(sabot,nb_carte,coord_y)

	elif sabot == 12 :
		valeur = valeur + 10
		image(sabot,nb_carte,coord_y)

	elif sabot == 13 :
		valeur = valeur + 10
		image(sabot,nb_carte,coord_y)

	elif sabot == 1 :
		image(sabot,nb_carte,coord_y)
		valeur = valeur

	else :
		valeur = valeur + sabot
		image(sabot,nb_carte,coord_y)

#Augmente le nb de carte de 1
	nb_carte = nb_carte + 1
#Change le texte des points du joueur
	valeur_string.set(f"Vous avez {valeur} points")



#Tirage des cartes
def sabot_ordi() :
	global nb_carte_ordi
	global valeur_ordi
	global carte_ordi
	global coord_y_ordi
	coord_y = coord_y_ordi[0]
	while valeur_ordi < 17:
	carte_cachee = False
		sabot = random.randint(1,13)

		if sabot == 11 :
			valeur_ordi = valeur_ordi + 10
			carte_ordi.append(sabot)
			if carte_cachee == False:
				image(sabot,nb_carte_ordi,coord_y)

		elif sabot == 12 :
			valeur_ordi = valeur_ordi + 10
			carte_ordi.append(sabot)
			if carte_cachee == False:
				image(sabot,nb_carte_ordi,coord_y)

		elif sabot == 13 :
			valeur_ordi = valeur_ordi + 10
			carte_ordi.append(sabot)
			if carte_cachee == False:
				image(sabot,nb_carte_ordi,coord_y)

		elif sabot == 1 :
			valeur_ordi = valeur_ordi
			carte_ordi.append(sabot)
			if carte_cachee == False:
				image(sabot,nb_carte_ordi,coord_y)
		else :
			valeur_ordi = valeur_ordi + sabot
			carte_ordi.append(sabot)
			if carte_cachee == False:
				image(sabot,nb_carte_ordi,coord_y)
			else:

		print(f"sabot {sabot}")
#Augmente le nb de carte de 1
		nb_carte_ordi = nb_carte_ordi + 1
	print(f"nb_carte_ordi {nb_carte_ordi}")


#------------------------------------------------------------#
# Fenetre master

fen = Tk()
fen.title('BlackJack')

#--------------------------------------------------------------#
# Tapis vert #

can = Canvas(fen, width =1030, height =800, bg ='sea green')
logo = PhotoImage(file="imgs/logo.gif")
can.create_image(515,425, image=logo)

#--------------------------------------------------------------#
# Variables Globales

nb_carte = 0
nb_carte_ordi = 0
valeur = 0
valeur_ordi = 0
liste_carte_img = []
carte_ordi = []

#--------------------------------------------------------------#
#Affichage du nb de point du joueur (Initatilisation)
valeur_string = StringVar()
valeur_affichage = Label( fen, textvariable=valeur_string)
valeur_string.set(f"Vous avez {valeur} point")
valeur_affichage.place(x = 448, y = 825)

#--------------------------------------------------------------#
# Boutons #

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').place(x = 1050, y = 30)
sabot_button = Button(fen,text='Carte',command=sabot, highlightbackground='#3E4149').place(x = 1050, y = 60)
Button(fen,text='Recommencer',command=restart_program, highlightbackground='#3E4149').place(x = 1050, y = 90)

sabot_ordi()
#--------------------------------------------------------------#
# Initatilisation de fenetre master
can.place(x = 0, y = 20)
fen.mainloop()
