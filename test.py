from random import *


def sabot() :
	choix = True
	valeur = 0

	while choix == True:
		sabot = randint(1, 13)
		if sabot == 11 :
			print("valet")
			valeur = valeur + 10

		elif sabot == 12 :
			print("dame")
			valeur = valeur + 10

		elif sabot == 13 :
			print("roi")
			valeur = valeur + 10

		elif sabot == 1 :
			valeur = valeur + 1

		else :
			print(sabot)
			valeur = valeur + sabot

		choix = int(input("Voulez vous une carte en plus \n 1. Oui \ 2. Non"))

		if choix == 1:
			choix = True
		else:
			choix = False

	print(valeur)

sabot()
