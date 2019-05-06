#coding : utf-8
import random
from tkinter import *
#---------------------------------------------------------------------#
def compte_joueur() :
	compte_courant = 500
	print("vous possédez actuellement",compte_courant," $")
	mise = int(input("combien voulez vous misez ?"))
	while mise > compte_courant :
		print("vous ne pouvez pas miser plus que vous ne possédez !")
		mise = int(input("Donc combien voulez vous vraiment miser ?"))
		return mise
	compte_courant == compte_courant - mise
	return compte_courant


#---------------------------------------------------------------------#
#valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11
#---------------------------------------------------------------------#
def assurance() :
	global mise_joueur
	global compte_courant
	assurance = mise_joueur%2
	compte_courant = compte_courant - assurance
	print("vous avez dsormais une assurance de",assurance,"$ ")
#---------------------------------------------------------------------#
def split() :
	global mise_joueur
	global compte_courant
	split = mise_joueur * 2
	compte_courant =- split
	pioche = carte_en_plus

#---------------------------------------------------------------------#
#pioche
def sabot() :

	valeur = 0
	sabot = random.randint(1, 13)
	if sabot == 11 :
		print("valet")
		valeur =+ 10
		return valeur

	elif sabot == 12 :
		print("dame")
		valeur =+ 10
		return valeur

	elif sabot == 13 :
		print("roi")
		valeur =+ 10
		return valeur

	elif sabot == 1 :                     #appelle la fonction as
		as_valeur = valeur_as()
		if as_valeur == 1 :
			valeur =+ 1
			return valeur
		else :
			valeur =+ 11
			return valeur

	else :
		print(sabot)
		valeur =+ sabot
		return valeur
#--------------------------------------------------------------------#
#possibilité de piocher des cartes en plus
def cartes_supplementaires() :
	cartes_supplementaires = int(input("Voulez vous une carte de plus ? \n 1 = oui \n 2 = non\n"))


def carte_en_plus() :
	global main_joueur
	while main_joueur < 21 :
		cartes_supplementaires = int(input("Voulez vous une carte en plus ? \n 1 = oui \n 2 = non\n"))
		while cartes_supplementaires == 1 :
			carte_en_plus = sabot()
			main_joueur =+ carte_en_plus
			print(main_joueur)
			return main_joueur
		while cartes_supplementaires == 2:
			break
	while main_joueur > 21 :
		print("perdu, vous avez dépassé 21")
	while main_joueur == 21 :
		print("vous ne devriez plus piochez de carte")
#--------------------------------------------------------------------#
#tour de distribution
def tour_de_distribution_1() :
	première_carte = sabot()
	seconde_carte = sabot()
	valeur_totale = première_carte + seconde_carte
	print(valeur_totale)
	return valeur_totale

#--------------------------------------------------------------------#
#choix après la distribution
def choix_partie() :

	choix = int(input("veuillez choisir une des option :\n 1 = Prendre l'assurance \n 2 = Effectuez un split \n 3 = Doubler votre mise \n 4 = ne rien faire \n"))
	if choix == 1 :
		assurance()
	elif choix == 2 :
		split()
	elif choix == 3 :
		doubler()
	while choix == 4 :
		break
	else :
		print("fait pas le malin billy bob")
		choix = choix_partie()
#--------------------------------------------------------------------#
#mise du joueur
mise_joueur = compte_joueur()
#--------------------------------------------------------------------#
#distribution des cartes au joueur
global main_joueur
main_joueur = tour_de_distribution_1()
carte_en_plus = carte_en_plus()
choix_partie = choix_partie()



#--------------------------------------------------------------------#
#choix pour la partie





#--------------------------------------------------------------------#
# TKinter
fen = Tk()
can = Canvas(fen, width =450, height =350, bg ='green')
can.grid(row=0,column=0)




fen.mainloop()
