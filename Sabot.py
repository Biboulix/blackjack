#coding : utf-8
import random
import pickle
import application
#---------------------------------------------------------------------#
#mise du joueur
mise_joueur = application.compte_joueur()
main_joueur = application.sabot()
while main_ordi < 17 :
	application.sabot()

if main_joueur < main_ordi :
	mise_joueur = 0 - mise_joueur


elif main_joueur == main_ordi :
	print("c'est une égalité. \n Vous repartez chacun avec votre mise ")

else :
	mise_joueur = mise_joueur * 2

	#---------------------------------------------------------------------#
with open("donnes, ab") as fichier :
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(mise)
	mon_pickler.close()
