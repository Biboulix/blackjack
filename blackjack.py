from tkinter import *
from bibli import *
import random
import sys
import os
import pickle

#---------------------------------------------------------------------------#
#Fonctions


#Valeur de l'as
def valeur_as() :

	vrai_valeur_as = int(input ("voulez vous que l'as valent 1 ou 11 ?")) #Chercher dans le terminal pour la valeur

	if vrai_valeur_as == 1 :
		print("Votre as vaut désormais 1")
		return vrai_valeur_as

	else :
		print("votre as vaut désormais 11")
		return 11

#Recommencer le programe
def restart_program(): #Prise depuis internet
	python = sys.executable
	os.execl(python, python, * sys.argv)

#--------------------------------------------------------------#
def afficher_carte_cachee():
    global liste_carte_img
    global coord_y_ordi
    global carte_ordi
    global nb_carte_ordi
    for k in range(0,nb_carte_ordi):
        #Choisir une carte dans le dossier cards
        carte = (carte_ordi[k]-1) * 4
        couleur = random.randint(0,3)
        carte_finale = carte + couleur
        img = PhotoImage(file=f"./cards/" + "card{}.gif".format(carte_finale)) #charge l'image de la carte
        liste_carte_img.append(img) #Crée une liste avec toutes les cartes générées (seulement pour les garder afficher)
        can.image= img
        can.create_image(coord_x[k],coord_y_ordi[0], image=img, anchor = NW) #Affiche la carte


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


def image_cache(nb_carte_ordi):
	global liste_carte_img
	global coord_y_ordi
	img = PhotoImage(file="./cards/back.gif")
	liste_carte_img.append(img)
	can.image= img
	can.create_image(coord_x[nb_carte_ordi],coord_y_ordi, image=img, anchor = NW)


def stop(): #Fonction qui s'active dès qu'on appuye sur le bouton stop
    global valeur
    global valeur_ordi
    #affiche les cartes dès qu'on appuye sur le boutton stop
    afficher_carte_cachee()

    if valeur > valeur_ordi and valeur <21: #Verifie si on a plus de point que l'ordi
        text = StringVar() #fonction tkinter pour pouvoir ajouter du text
        text_affichage = Label( fen, textvariable=text) #Creer un label avec la variable text dedans
        text.set(f"Vous avez gagné") #Change la variable text en "Vous avez gangé"
        text_affichage.place(x = 1050, y = 425,anchor = W) #PLace le label en coordonées x = 1050 et y = 425

    elif valeur_ordi > valeur and valeur_ordi<21: #Verifie si on a moins de point que l'ordi
        text = StringVar()
        text_affichage = Label( fen, textvariable=text)
        text.set(f"Vous avez perdu")
        text_affichage.place(x = 1050, y = 425,anchor = W)
    elif valeur == 21:
        text = "Vous avez gagné avec un blackjack"
        label = Label( fen, text = text )
        label.place(x = 1050, y = 425,anchor = W)
    elif valeur_ordi == 21:
        text = "L'ordi a gagné avec un blackjack"
        label = Label( fen, text = text )
        label.place(x = 1050, y = 425,anchor = W)
    else:
        text = StringVar()
        text_affichage = Label( fen, textvariable=text)
        text.set(f"Egalité")
        text_affichage.place(x = 1050, y = 425,anchor = W)


def verification(valeur = 0, valeur_ordi=0): #Verifie si l'ordi ou nous avons dépassé les 21

    if valeur > 21: #Si on depasse les 21
        afficher_carte_cachee() #affiche toutes les cartes cachées
        text = "Vous avez perdu"
        label = Label( fen, text = text )
        label.place(x = 1050, y = 425,anchor = W)
        perdu = True
        return perdu #Pour la boucle dans Sabot

    elif valeur_ordi > 21: #Si l'ordi depasse les 21
        afficher_carte_cachee()
        text = "L'ordi a perdu"
        label = Label( fen, text = text )
        label.place(x = 1050, y = 425,anchor = W)


    else:
        perdu = False
        return perdu




#Tirage des cartes
def sabot() :
    global nb_carte
    global valeur
    global valeur_string
    global perdu

    sabot = random.randint(1,13) #génère une valeur de carte


    if perdu == False:
        if sabot == 11 :
            valeur = valeur + 10
            image(sabot,nb_carte,600) #chercher la fonciton image qui affiche les cartes


        elif sabot == 12 :
            valeur = valeur + 10
            image(sabot,nb_carte,600)

        elif sabot == 13 :
            valeur = valeur + 10
            image(sabot,nb_carte,600)

        elif sabot == 1 :

            image(sabot,nb_carte,600)
            sabot = valeur_as()
            valeur = valeur + sabot

        else:
            valeur = valeur + sabot
            image(sabot,nb_carte,600)

        perdu = verification(valeur) #Si perdu == True => peut plus piocher de carte meme en appuyant sur le bouton


    #Augmente le nb de carte de 1
    nb_carte = nb_carte + 1
    #Change le texte des points du joueur
    valeur_string.set(f"Vous avez {valeur} points")



#Tirage des cartes
def sabot_ordi() : #Comme Sabot pour le joueur mais avec des parties TK spécialement pour l'ordi
    global nb_carte_ordi
    global valeur_ordi
    global carte_ordi
    global valeur
    carte_cachee = False #Dit que la première carte doit être face visible
    while valeur_ordi < 17:

        sabot = random.randint(1,13)

        if sabot == 11 :
            valeur_ordi = valeur_ordi + 10

            carte_ordi.append(sabot) #Liste des cartes tirés pas l'ordi pour afficher les cartes en face visible après

            if carte_cachee == False: #Affiche la carte face visible
                image(sabot,nb_carte_ordi,15) #La place avec la fonction image expliqué avant
            else:
                image_cache(nb_carte_ordi) #Si la carte doit être afficher face cachée utilise la fonction spéciale

        elif sabot == 12 :
            valeur_ordi = valeur_ordi + 10
            carte_ordi.append(sabot)
            if carte_cachee == False:
                image(sabot,nb_carte_ordi,15)
            else:
                image_cache(nb_carte_ordi)

        elif sabot == 13 :
            valeur_ordi = valeur_ordi + 10
            carte_ordi.append(sabot)
            if carte_cachee == False:
                image(sabot,nb_carte_ordi,15)
            else:
                image_cache(nb_carte_ordi)

        elif sabot == 1 :
            valeur_as = 11 #Prends 11 comme valeur de l'as
            valeur_test = valeur_as + valeur_ordi
            if valeur_test > 21:  #Si avec 11 valeur dépasse 21 alors prends as comme 1
                valeur_as = 1
                valeur_ordi = valeur_as + valeur_ordi
            else:
                valeur_ordi = valeur_as + valeur_ordi

            carte_ordi.append(sabot)

            if carte_cachee == False:
                image(sabot,nb_carte_ordi,15)
            else:
                image_cache(nb_carte_ordi)


        else :
            valeur_ordi = valeur_ordi + sabot
            carte_ordi.append(sabot)
            if carte_cachee == False:
                image(sabot,nb_carte_ordi,15)
            else:
                image_cache(nb_carte_ordi)


        carte_cachee = True #Pour qu'après la première carte les cartes soient face cachés
        #Augmente le nb de carte de 1
        nb_carte_ordi = nb_carte_ordi + 1

        verification(valeur,valeur_ordi)  #Verifie si on a pas déapssé les 21


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
perdu = False
#--------------------------------------------------------------#
#Affichage du nb de point du joueur (Initatilisation)
valeur_string = StringVar()
valeur_affichage = Label( fen, textvariable=valeur_string)
valeur_string.set(f"Vous avez {valeur} point")
valeur_affichage.place(x = 448, y = 825)

#---------------------#
#Lance la pioche de l'ordi
sabot_ordi()

#--------------------------------------------------------------#
# Boutons affichages des boutons

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').place(x = 1050, y = 30) #quitte la fen principale de tkinter
Button(fen,text='Carte',command=sabot, highlightbackground='#3E4149').place(x = 1050, y = 60)
Button(fen,text='Recommencer',command=restart_program, highlightbackground='#3E4149').place(x = 1050, y = 90)
Button(fen,text='Stop', command=stop ,highlightbackground='#3E4149').place(x = 1050, y = 120)


#--------------------------------------------------------------#
# Initatilisation de fenetre master
can.place(x = 0, y = 20)
fen.mainloop()
