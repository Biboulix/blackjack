import random
import pickle
from bibli import *
from tkinter import *

def compte_joueur() :
	with open("donnees", "rb") as fichier :
		mon_depickler = pickle.Unpickler(fichier)
		mon_dico_joueur = mon_depickler.load()

		mon_pseudo = input("Veuillez entrer votre pseudo : \n ")
		if mon_pseudo in mon_dico_joueur.keys() :
			mon_score = mon_dico_joueur[mon_pseudo]
		else :
			mon_dico_joueur[mon_pseudo] = 500
			mon_score = mon_dico_joueur[mon_pseudo]

	print("vous possédez actuellement",mon_dico_joueur[mon_pseudo]," $")
	mise = int(input("combien voulez vous misez ?"))
	while mise > mon_score :
		print("vous ne pouvez pas miser plus que vous ne possédez !")
		mise = int(input("Donc combien voulez vous vraiment miser ?"))
		return mise
		mon_score =- mise
		return mon_score

#Recommencer le programe
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

#Valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11

#Affichage des cartes
def image(sabot,nb_carte):
    global liste_carte_img
    carte = (sabot-1) * 4
    couleur = random.randint(0,3)
    carte_finale = carte + couleur
    img = PhotoImage(file=f"./cards/" + "card{}.gif".format(carte_finale))
    liste_carte_img.append(img)
    can.image= img
    can.create_image(coord_x[nb_carte],coord_y_joueur[0], image=img, anchor = NW)

#Tirage des cartes
def sabot() :
    global nb_carte
    global valeur
    global valeur_string

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
        image(sabot,nb_carte)
        valeur = valeur

    else :
        valeur = valeur + sabot
        image(sabot,nb_carte)


    #Augmente le nb de carte de 1
    nb_carte = nb_carte + 1

    #Change le texte des points du joueur
    valeur_string.set(f"Vous avez {valeur} points")


def blackjack() :
	global main_joueur
	global mise_joueur
	if main_joueur == 21 :
		print("vous avez un blackjack")
		mise_joueur = mise_joueur * 2
		return mise_joueur






#Variables
nb_carte = 0
valeur = 0
liste_carte_img = []
