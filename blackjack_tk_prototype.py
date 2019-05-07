from tkinter import *








#------------------------------------------------------------#
# Fenetre master

fen = Tk()
fen.title('BlackJack')
#--------------------------------------------------------------#
# Tapis vert #

can = Canvas(fen, width =1030, height =850, bg ='sea green')
can.grid(row=0,column=0)
img = PhotoImage(file="logo.gif")
can.create_image(515,425, image=img)
#--------------------------------------------------------------#
# Positions pour les cartes #
#Coordonées de la position de l'ange NW

coord_x = [50,210,370,530,690,850,130,290,450,610,770]

coord_y_ordi = [15,210] #15 pour la ligne du haut (carte 1 - 6), 210 pour la ligne du bas (carte 7-11)

coord_y_joueur = [650, 455] #650 pour la ligne du bas (carte 1 - 6), 455 pour la ligne du haut (carte 7-11)

#--------------------------------------------------------------#
# Case blanches haut #

x1,y1,x2,y2 = 50,15,175,200
x3,y3,x4,y4 = 130,210,255,395
for f in range(0,6):
    can.create_rectangle(x1,y1,x2,y2,outline="snow")
    x1,x2 = x1+160, x2+160
for f in range(0,5):
    can.create_rectangle(x3,y3,x4,y4,outline="snow")
    x3,x4 = x3+160, x4+160
# Case blanches bas #

x5,y5,x6,y6 = 130,455,255,640
x7,y7,x8,y8 = 50,650,175,835
for f in range(0,5):
    can.create_rectangle(x5,y5,x6,y6,outline="snow")
    x5,x6 = x5+160, x6+160
for f in range(0,6):
    can.create_rectangle(x7,y7,x8,y8,outline="snow")
    x7,x8 = x7+160, x8+160

#--------------------------------------------------------------#
# Test de posage de cartes


image = PhotoImage(file="cards/roi/roi_coeur.gif")
can.create_image(coord_x[3],coord_y_ordi[0], image = image, anchor=NW)


#--------------------------------------------------------------#
# Bouton #

Button(fen,text='Quitter',command=fen.quit, highlightbackground='#3E4149').grid(row=0,column=1)

#--------------------------------------------------------------#
# Initatilisation de fenetre master

fen.mainloop()
