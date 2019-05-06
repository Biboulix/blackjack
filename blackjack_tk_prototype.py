from tkinter import *








#------------------------------------------------------------#
# Fenetre master

fen = Tk()

#--------------------------------------------------------------#
# Tapis vert #

can = Canvas(fen, width =1430, height =850, bg ='sea green')
can.grid(row=0,column=0)
img = PhotoImage(file="logo.gif")
can.create_image(715,425, image=img)

#--------------------------------------------------------------#
# Case blanches #

x1,y1,x2,y2 = 15,15,155,300
x3,y3,x4,y4 = 15,555,155,840
for f in range(0,9):
    can.create_rectangle(x1,y1,x2,y2,outline="snow")
    x1,x2 = x1+158, x2+158
for f in range(0,9):
    can.create_rectangle(x3,y3,x4,y4,outline="snow")
    x3,x4 = x3+158, x4+158

#--------------------------------------------------------------#
# Initatilisation de fenetre master

fen.mainloop()
