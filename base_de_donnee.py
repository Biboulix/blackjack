
import pickle

# on récupère le dictionnaire des "joueur" : score
with open("candidats","wb") as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    mon_dico_joueurs = mon_depickler.load()
#print(mon_dico_joueurs)

# récuperation des données du joueur avec création éventuelle
mon_pseudo = input("Entrez votre pseudo : ")
if mon_pseudo in mon_dico_joueurs.keys():
    mon_score = mon_dico_joueurs[mon_pseudo]
else:
    mon_dico_joueurs[mon_pseudo] = 500

print("Bonjour {}, l'état de votre compte courant actuel est {}.".format(mon_pseudo,mon_dico_joueurs[mon_pseudo]))




    #if mot_en_cours == mot_a_trouver :
        #gain += nombre_coups_max - compteur_coups
        #print("Bravo, vous avez trouvé le bon mot. Votre score personnel augmente de {} point(s)".format(gain))



        #mon_dico_joueurs[mon_pseudo] = gain
        # Gestion de l'etat du compte


        #trouve = True





# on met à jour le dictionnaire des "joueur" : score
with open("donnees","wb") as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(mon_dico_joueurs)
