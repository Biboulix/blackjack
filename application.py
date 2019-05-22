import random
import pickle
from bibli import *
from tkinter import *



#Valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?"))

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11
