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

with open("donnes, wb") as fichier :
	mon_pickler = pickle.Pickler(fichier)
	mon_pickler.dump(mise_joueur)
	mon_pickler.close()
