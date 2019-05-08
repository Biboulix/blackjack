#coding : utf-8
import random
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
	choix = True
	valeur = 0
	while choix == True:
		print("Total ", valeur)
		sabot = random.randint(1, 13)
		if sabot == 11 :
			print("valet")
			valeur = valeur + 10


		elif sabot == 12 :
			print("dame")
			valeur = valeur + 10


		elif sabot == 13 :
			print("roi")
			valeur = valeur + 10


		elif sabot == 1 :                     #appelle la fonction as
			as_valeur = valeur_as()
			if as_valeur == 1 :
				valeur = valeur + 1

			else :
				valeur = valeur + 11

		else :
			print(sabot)
			valeur = valeur + sabot

		choix = int(input("Voulez vous une carte en plus \n 1. Oui \n 2. Non \n"))
		if choix == 1:
			choix = True
		else:
			choix = False

	print("Vous avez un total de ", valeur)


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

sabot()
#--------------------------------------------------------------------#
#distribution des cartes au joueur
choix_partie = choix_partie()

#--------------------------------------------------------------------#
#choix pour la partie
