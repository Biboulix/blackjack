import random
import pickle

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
#--------------------------------------------------------------------#
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11
#--------------------------------------------------------------------#
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
