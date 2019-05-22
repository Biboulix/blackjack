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


#Valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11
