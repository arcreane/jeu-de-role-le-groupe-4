# Import module
from tkinter import *
import tkinter
from tkinter.font import Font
import winsound
from tkinter import messagebox
import numpy as np
from PIL import Image
from resizeimage import resizeimage
# Create object
root = Tk()

# Adjust size
root.geometry("1000x750")
# root.resizable(0,0)

# Create canvas___________________________________________________________________________________________________
canvas = Canvas( root, width = 800, height = 600)
canvas.pack(fill = "both", expand = True)

# Variables_______________________________________________________________________________________________________
array = []
Score = 0
lifeOfUser = 3
fadre = Font(family='Helvetica', size=24, weight='bold')
titre = Font(family='Times', size=58, weight='bold')
recit = Font(family='Times', size=18, weight='bold')
titre1 = Font(family='Times', size=30, weight='bold')
                    #---------Code pour compréhension---------#
                    #            4 pour les ennemis           #
                    #            5 pour l'argent              #
                    #            8 pour la sortie EXIT        #
                    #            9 pour le héros              #
                    #            0 pour un mur                #
                    #            1 pour un mur blanc          #
                    #-----------------------------------------#
# Fonction________________________________________________________________________________________________________

def moveRight(event):
    global array,Score, lifeOfUser
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9 or array[pig1][pig2] ==6:
                number.append(pig1)
                number.append(pig2)
    if array[number[0]][number[1]+1] == 1 or array[number[0]][number[1]+1] == 5:
        if array[number[0]][number[1]+1] == 5:
            Score += 20
            winsound.PlaySound("./sound/coin4.wav",winsound.SND_FILENAME)
        elif array[number[0]-1][number[1]] == 1:
            winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
        array[number[0]][number[1]+1] = 9
        array[number[0]][number[1] + 1] = 6
        array[number[0]][number[1]] = 1
    elif array[number[0]][number[1]+1]==4:
       
        array[number[0]][number[1]+1] = 9
        array[number[0]][number[1] + 1] = 6
        array[number[0]][number[1]] = 1
        lifeOfUser-=1
    if array[number[0]][number[1]+1] == 8:
        winsound.PlaySound("./sound/gameover5.wav",winsound.SND_FILENAME)
        part4a(event)
    if lifeOfUser<1:
        messagebox.showinfo(message="Vous avez perdu")
        commencer(event)
    canvas.delete("gp")
    canvas.delete("pig")
    drawing()
def moveLeft(event):
    global array,Score,lifeOfUser
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9 or array[pig1][pig2] ==6:
                number.append(pig1)
                number.append(pig2)
    if array[number[0]][number[1]-1] == 1 or array[number[0]][number[1]-1] == 5:
        if array[number[0]][number[1]-1] == 5:
            Score += 20
            winsound.PlaySound("./sound/coin4.wav",winsound.SND_FILENAME)
        elif array[number[0]-1][number[1]] == 1:
            winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
        array[number[0]][number[1]-1] = 9
        array[number[0]][number[1] - 1] = 6
        array[number[0]][number[1]] = 1
    elif array[number[0]][number[1]-1]==4:
        winsound.PlaySound("./sound/error2.wav",winsound.SND_FILENAME)
        array[number[0]][number[1]-1] = 9
        array[number[0]][number[1] - 1] = 6
        lifeOfUser-=1
        array[number[0]][number[1]-1] = 1
    if array[number[0]][number[1]-1] == 8:
        winsound.PlaySound("./sound/gameover5.wav",winsound.SND_FILENAME)
        part3a(event)
    if lifeOfUser<1:
        messagebox.showinfo(message="Vous avez perdu")
        commencer(event)
    canvas.delete("gp")
    canvas.delete("pig")
    drawing()
def moveDown(event):
    global array,Score,lifeOfUser, part2a
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9 or array[pig1][pig2] ==6:
                number.append(pig1)
                number.append(pig2)
    if array[number[0]+1][number[1]] == 1 or array[number[0]+1][number[1]] == 5:
        if array[number[0]+1][number[1]] == 5:
            Score += 20
            winsound.PlaySound("./sound/coin4.wav",winsound.SND_FILENAME)
        elif array[number[0]-1][number[1]] == 1:
            winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
        array[number[0]+1][number[1]] = 9
        array[number[0] + 1][number[1]] = 6
        array[number[0]][number[1]] = 1
    elif array[number[0]+1][number[1]]==4:
        winsound.PlaySound("./sound/error2.wav",winsound.SND_FILENAME)
        array[number[0]+1][number[1]] = 9
        array[number[0] + 1][number[1]] = 6
        lifeOfUser-=1
        array[number[0]][number[1]] = 1
    if array[number[0]+1][number[1]] == 8:
        winsound.PlaySound("./sound/secret4.wav",winsound.SND_FILENAME)
        part2a(event)
    if lifeOfUser<1:
        messagebox.showinfo(message="Vous avez perdu")
        commencer(event)
    canvas.delete("gp")
    canvas.delete("pig")
    drawing()
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
def moveUp(event):
    global array,Score,lifeOfUser
    X = 0
    Y = 50
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9 or array[pig1][pig2] ==6 :
                number.append(pig1)
                number.append(pig2)
    if array[number[0]-1][number[1]] == 1 or array[number[0]-1][number[1]] == 5:
        if array[number[0]-1][number[1]] == 5:
            Score += 20
            winsound.PlaySound("./sound/coin4.wav",winsound.SND_FILENAME)
        elif array[number[0]-1][number[1]] == 1:
            winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
        array[number[0]-1][number[1]] = 9
        array[number[0] - 1][number[1]] = 6
        array[number[0]][number[1]] = 1
    elif array[number[0]-1][number[1]]==4:
        winsound.PlaySound("./sound/error2.wav",winsound.SND_FILENAME)
        array[number[0]-1][number[1]] = 9
        array[number[0] - 1][number[1]] = 6
        lifeOfUser-=1
        array[number[0]][number[1]] = 1
    if array[number[0]-1][number[1]] == 8:
        winsound.PlaySound("./sound/gameover5.wav",winsound.SND_FILENAME)

    if lifeOfUser<1:
        winsound.PlaySound("./sound/gameover5.wav",winsound.SND_FILENAME)
        messagebox.showinfo(message="Vous avez perdu")
        commencer(event)


    canvas.delete("gp")
    canvas.delete("pig")
    drawing()
def Exit(event):
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
    canvas.delete("exit")
    canvas.delete("farm")
    canvas.delete("gp")
    canvas.delete("pig")
    canvas.delete("score")
    canvas.delete("heart")
    # start()

def drawing():
    global array, cocos, lifeOfUser
    
    canvas.create_image( 0, 0, image = cocos, anchor = "nw", tags="farm")
    number = []
    X = 0
    Y = 50
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 6:
                canvas.create_rectangle(X, Y, X + 30, Y + 30, fill="white", tags="gp")
                canvas.create_image(X, Y, image=piggy1, anchor="nw", tags="pig1")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            elif array[index1][index2] == 4:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
                canvas.create_image( X, Y-7, image = Enemy, anchor = "nw", tags="gp")
            elif array[index1][index2] == 5:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
                canvas.create_image( X, Y, image = coin , anchor = "nw", tags="gp")
                
            X +=30
        Y += 30
        X = 0
        
    canvas.create_rectangle(0, 0, 80, 40, outline="black", fill="orange", tags="exit")
    canvas.create_text(40, 20, text = "Back", fill="darkblue", font="consolas 15", tags="exit")
    canvas.create_image(800,5, image=life , anchor = "nw", tags="heart")
    canvas.create_text(840,12, text=str(lifeOfUser), anchor = "nw", tags="heart")
    canvas.delete("score")
    canvas.create_text(650, 20, text = "Your score: "+str(Score), fill="darkblue", font="consolas 15", tags="score")
    

def part1(event):
    global array,lifeOfUser
    lifeOfUser = 3
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 5, 5, 5, 9, 0, 5, 5, 5, 0, 5, 5, 0, 5, 5, 5, 5, 0],
             [0, 5, 5, 0, 5, 0, 5, 5, 0, 5, 5, 0, 5, 0, 0, 0, 8, 0, 5, 0, 5, 5, 5, 5, 4, 5, 0, 5, 0, 0],
             [0, 5, 5, 0, 4, 0, 0, 5, 5, 4, 5, 0, 5, 5, 5, 5, 5, 0, 5, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 0],
             [0, 0, 5, 0, 0, 5, 5, 0, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 0, 5, 0, 5, 0, 5, 0, 0, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0, 5, 0, 4, 0, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 4, 5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 4, 0, 5, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 4, 5, 0, 5, 0, 5, 5, 0, 5, 0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 5, 5, 0, 4, 0],
             [0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 0, 0, 0, 5, 0, 5, 0, 5, 0],
             [0, 5, 5, 0, 5, 0, 5, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 0, 0, 5, 0, 5, 0, 5, 0, 5, 0, 0, 0],
             [0, 5, 5, 5, 5, 5, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 0, 0, 5, 0, 5, 0],
             [0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0, 5, 0, 0, 0, 5, 0, 5, 0, 5, 0],
             [0, 5, 5, 5, 0, 5, 0, 5, 5, 4, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 5, 5, 0],
             [0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 0, 5, 0, 0, 0],
             [0, 5, 0, 5, 5, 4, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 0, 5, 0, 0, 5, 5, 5, 0, 5, 0],
             [0, 5, 5, 5, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 5, 0, 5, 0, 5, 5, 5, 0],
             [0, 5, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 4, 5, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0]]
    drawing()
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)

def part2(event):
    global array,lifeOfUser
    lifeOfUser = 3
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [8, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 4, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 0],
             [0, 5, 0, 5, 0, 0, 0, 0, 5, 0, 5, 5, 5, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0],
             [0, 5, 0, 5, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 5, 5, 5, 4, 0, 5, 5, 5, 5, 5, 0, 5, 0],
             [0, 5, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 4, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 0, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 5, 5, 0],
             [0, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 0, 5, 0, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0],
             [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 5, 5, 0, 5, 0, 5, 5, 0, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 4, 0, 5, 0],
             [0, 5, 0, 5, 0, 4, 5, 5, 5, 0, 0, 0, 5, 5, 5, 0, 5, 0, 0, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0, 5, 5, 0],
             [0, 5, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 4, 0, 5, 0, 5, 5, 5, 0, 0, 5, 0, 0, 0, 5, 0, 5, 0, 0, 5, 0],
             [0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 0, 5, 0, 0, 0, 5, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 0],
             [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 5, 0],
             [0, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5, 4, 0, 5, 0, 5, 0, 0, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0],
             [0, 5, 0, 5, 0, 5, 5, 5, 5, 0, 5, 0, 5, 0, 5, 0, 5, 5, 5, 4, 0, 5, 5, 5, 5, 0, 5, 5, 0, 5, 5, 0],
             [0, 4, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0],
             [0, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 0, 5, 5, 0, 8, 9, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    drawing()
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)

def part3(event):
    global array,lifeOfUser
    lifeOfUser = 3
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0],
             [0, 9, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
             [0, 0, 0, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0],
             [0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 0, 5, 8],
             [0, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 4, 0, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 5, 0, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 0],
             [0, 5, 5, 0, 5, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 5, 5, 0, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 0, 5, 0, 5, 0, 0],
             [0, 0, 0, 5, 5, 5, 0, 5, 5, 5, 5, 4, 0, 5, 5, 0, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 5, 0],
             [0, 5, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0],
             [0, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0],
             [0, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 5, 4, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0],
             [0, 5, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 4, 5, 5, 5, 5, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    drawing()
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)

def part4(event):
    global array, lifeOfUser
    lifeOfUser = 3
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 0],
             [0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
             [0, 0, 0, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 0, 5, 5, 0, 5, 0],
             [0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 4, 0, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 5, 0, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 0],
             [0, 5, 5, 0, 5, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5, 0, 5, 0, 0],
             [0, 5, 5, 0, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 5, 0, 5, 5, 0, 5, 0, 5, 0, 5, 0, 0],
             [0, 0, 0, 5, 5, 5, 0, 5, 5, 5, 5, 4, 0, 5, 5, 0, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 5, 0],
             [0, 5, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0],
             [0, 5, 5, 5, 0, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0],
             [0, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 5, 4, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 0, 5, 0],
             [0, 5, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0],
             [0, 5, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 0],
             [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0],
             [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 0, 5, 9, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    drawing()
    winsound.PlaySound("./sound/rockHit2.wav", winsound.SND_FILENAME)


def comeback(event):
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
    canvas.delete("part1")
    canvas.delete("part2")
    canvas.delete("part3")
    canvas.delete("personnaliser")
    canvas.delete("Back")
    graphic()


def SetBack(event):
    canvas.delete("setting")
    canvas.delete("SetBack")
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)


def Tutoriel(event):
    canvas.create_rectangle(100, 150,900,650, outline="black", fill="white", tags="Tutoriel")
    canvas.create_text(500,280, text = "Fonctionnement du jeu", fill="black", font="consolas 15 bold", tags="Tutoriel")
    canvas.create_text(500,350, text = "1. Pour gagner, il faut aller jusqu'au bloc EXIT.", fill="black", font="consolas 15", tags="Tutoriel")
    canvas.create_text(500,400, text = "2. Plus vous ramassez de pièces, plus vous en aurez pour votre famille.", fill="black", font="consolas 15", tags="Tutoriel")
    canvas.create_text(500,450, text = "3. Si vous n'arrivez pas à la sortie, alors vous perdrez.", fill="black", font="consolas 15", tags="Tutoriel")
    canvas.create_text(500,500, text = "4. Chaque ennemi vous enlève un coeur. A 0 coeur, vous avez perdu", fill="black", font="consolas 15 ", tags="Tutoriel")
    
    canvas.create_rectangle(220, 170, 290, 220, fill="orange", outline="black", tags ="ScenBack")
    canvas.create_text(255,195, text = "Back", fill="black", font="consolas 15 ", tags="ScenBack")
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)


def ScenBack(event):
    canvas.delete("ScenBack")
    canvas.delete("Tutoriel")
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)

def commencer(event):
    global bgpig
    canvas.create_image( 0, 0, image = bgpig, anchor = "nw")
    canvas.create_text(500, 80, text="A vous le choix de votre aventure", fill="#DC72DC", font=fadre)
    canvas.create_rectangle(10, 430, 410, 510, outline="black", fill="white", tags="part1a")
    canvas.create_text(210, 470, text = "Jouer à l'histoire", fill="black", font="consolas 30", tags="part1a")

    canvas.create_rectangle(270, 690, 730, 610, outline="black", fill="white", tags="personnaliser")
    canvas.create_text(500, 650, text="Créer votre histoire", fill="black", font="consolas 28 ", tags="personnaliser")

    canvas.create_rectangle(20, 10, 100, 50, outline="black", fill="orange", tags="Back")
    canvas.create_text(55,30, text = "Back", fill="darkblue", font="consolas 15", tags="Back")
    winsound.PlaySound("./sound/rockHit2.wav",winsound.SND_FILENAME)
    canvas.tag_bind("part1a", "<Button-1>", part1a)
    canvas.tag_bind("part2a", "<Button-1>", part2a)
    canvas.tag_bind("part3a", "<Button-1>", part3a)
    canvas.tag_bind("part4a", "<Button-1>", part4a)

def back(event):
    winsound.PlaySound("./sound/rockHit2.wav", winsound.SND_FILENAME)
    canvas.delete("part1")
    canvas.delete("part2")
    canvas.delete("part3")
    canvas.delete("personnaliser")
    graphic()


# Images____________________________________________________________________________________________________

#bg = PhotoImage(file = "./Images/farmpig.gif")
bg = PhotoImage(master=root, file = "./Images/farmpig.gif")
bgpig = PhotoImage(master=root,file = "./Images/three_pig.gif")
bgfarm = PhotoImage(master=root,file = "./Images/backpig.gif")
wall = PhotoImage(master=root,file = "./Images/brickBrown.png")
piggy = PhotoImage(master=root,file = "./Images/piggy.gif")
piggy1 = PhotoImage(master=root,file = "./Images/piggy1.gif")
Exitway = PhotoImage(master=root,file = "./Images/signExits.png")
Enemy = PhotoImage(master=root,file = "./Images/malePerson_walk0.png")
coin = PhotoImage(master=root,file="./Images/coin.png")
life = PhotoImage(master=root,file="./Images/life.png")
wallcity = PhotoImage(master=root,file="./Images/ville.png")
ponts = PhotoImage(master=root,file="./Images/ponts.png")
cocos = PhotoImage(master=root,file="./Images/cocos.png")
forges = PhotoImage(master=root,file="./Images/froges.png")
murs = PhotoImage(master=root,file="./Images/murs.png")
scients = PhotoImage(master=root,file="./Images/scients.png")
domaines = PhotoImage(master=root,file="./Images/domaines.png")
tunnels = PhotoImage(master=root,file="./Images/tunnels.png")
soleils = PhotoImage(master=root,file="./Images/soleils.png")

def part1a(event):
    canvas.create_image(500, 375, image = ponts, anchor = "center")
    image = Image.open('./Images/ponts.png')
    canvas.create_text(500, 150, text = "Premier porte : Le pont-levis", fill="#C0A6A6", font=titre)
    canvas.create_text(510, 350, text = "Réussite : « Accès à la salle des commandes du pont-levis. »\n\n\nÉchec : « Vous mourrez. \nLes cochons rebelles ne peuvent pas passer le pont-levis.\nIls se noient, sont appréhendés\net envoyé à l’abattoir. »", fill="black", tags="part1", font=recit)
    winsound.PlaySound("./sound/porte1.wav", winsound.SND_ASYNC)

def part2a(event):
    canvas.create_image( 0, 0, image = forges, anchor = "nw")
    image = Image.open('./Images/froges.png')
    canvas.create_text(515, 100, text = "Deuxième porte : Armes de technologie graisseuse", fill="white", font=titre1)
    canvas.create_text(515, 350, text = "Réussite : « Accès à la salle de commandes permettant de désactiver\nles armes de technologies graisseuses et rendant les humains vulnérables. »\n\n\nÉchec : « « Vous mourrez. Les cochons rebelles peuvent passer le pont-levis,\n mais ils se font trucider par les armes de technologies graisseuse ou envoyer à l’abattoir.  »", fill="#FFFFFF", tags="part2", font=recit)
    winsound.PlaySound("./sound/porte2.wav", winsound.SND_ASYNC)

def part3a(event):

    canvas.create_image( 0, 0, image = murs, anchor = "nw")
    image = Image.open('./Images/murs.png')
    canvas.create_text(515, 100, text = "Troisième porte : Les murailles de PigCity et des fermes", fill="white", font=titre1)
    canvas.create_text(515, 350, text = "Réussite : « Accès à la salle de commandes\n permettant de désactivé les murailles et de libérés la société animale. »\n\n\nÉchec : « Vous mourrez. Les cochons rebelles se retrouvent encerclés sans échappatoire,\n ils sont appréhendés et envoyé à l’abattoir. »", fill="#FFFFFF", tags="part3", font=recit)
    winsound.PlaySound("./sound/porte3.wav", winsound.SND_ASYNC)

def part4a(event):

    canvas.create_image( 0, 0, image = scients, anchor = "nw")
    image = Image.open('./Images/scients.png')
    canvas.create_text(515, 100, text = "                        Quatrième porte :\n Puces implémenter dans le corps des animaux ", fill="white", font=titre1)
    canvas.create_text(515, 350, text = "Réussite : « Accès à la salle de commandes permettant de désactivé les puces,\n rendant ainsiles animaux totalement libre de leur mouvement.  »\n\n\nÉchec : « Vous mourrez.\n Les cochons rebelles se retrouvent encerclés sans échappatoire,\n ils sont appréhendés et envoyé à l’abattoir. »", fill="#FFFFFF", tags="part4", font=recit)
    winsound.PlaySound("./sound/porte4.wav", winsound.SND_ASYNC)

def part5a(event):
    canvas.create_image(500, 375, image = soleils, anchor = "center")
    image = Image.open('./Images/soleils.png')
    canvas.create_text(500, 150, text = "Réussite finale", fill="#C0A6A6", font=titre)
    canvas.create_text(510, 350, text = "Les cochons ont réussis à prendre le contrôle du quartier générale. Les Hommes\n tyranniques sont démunis. Sans leurs technologies graisseuses, ils sont impuissants. Rond\n comme des ballons, il ne peuvent que roulé approximativement. La mémoire de tout les\n cochons et animaux massacrer durant des siècles est commémorer. On salue leurs bravoures\n et leurs haines qui à contribuer au gonflement des hommes, jusqu’à les rendre impuissants sans\n l’aide de la technologie. \nLa plupart des cochons devienne nomade et part découvrir le monde. Ce sont les cochons\n voyageurs. Certains, décident de se sédentariser et de créer une société stable et libre, à\n commencer par la capitale, Liberty-City, où vivent différentes espèces animales. \n\nLes cochons voyageurs, prennent la mer et découvrent par de-là les continents des Hommes\n d’une autres espèces, les végé-terriens. Ainsi, Ils devinrent copains comme cochon. \n", fill="black", tags="part1", font=recit)
    winsound.PlaySound("./sound/porte5.wav", winsound.SND_ASYNC)


def histoire(event):
    canvas.create_image(500, 375, image = wallcity, anchor = "center")
    image = Image.open('./Images/ville.png')
    new_image = image.resize((1000, 750))
    new_image.save('./Images/villes.png')
    canvas.create_text(515, 100, text = "Piggy Adventure", fill="black", font=titre)
    canvas.create_text(515, 350, text = "Dans un monde régit par les humains, les cochons sont des proies. Leurs unique moyen de\n survit, l’argent et l’agilité. Au village des cochons, « PigCity » un semblant de paix et de libertés\n s’est installé sous le couvert d’impôts obligatoire, récolter par les humains. La ville\n est entouré d’une grande muraille similaire à la muraille de Chine, sur laquelle des patrouilles\n surveille la vie à l’intérieur de l’enceinte de la cité. Ces impôts leurs servent\n ensuite à financer leurs élevage intensif de cochon et autre animaux de fermes. Ces pauvres\n cochons gagnent leurs libertés à l’insu de la mort de leurs confrère qui s’attèle à remplir la\n panse des Hommes tyranniques.", fill="#FFFFFF", tags="par1", font=recit)
    winsound.PlaySound("./sound/part1.wav", winsound.SND_ASYNC)

def par1(event):

    canvas.create_image( 0, 0, image = scients, anchor = "nw")
    image = Image.open('./Images/scients.png')
    canvas.create_text(515, 100, text = "Piggy Adventure", fill="black", font=titre)
    canvas.create_text(515, 350, text = "Les Hommes après des siècles de tyrannie, ont développés des armes technologiques qui\n fonctionne à la graisse de cochons et qui leurs permet des les maitriser sans user de leurs\n capacités motrices. Ainsi, les humains on atteint une nouvel évolution de l’espèce qui n’utilise\n pas les muscles. Cela a eu pour effet de transformer les Hommes en boules de\n masse graisseuse consommatrice de cochons, dont la haine alimente la baisse des capacités\n mouvante de l’Homme. ", fill="#FFFFFF", tags="par2", font=recit)
    winsound.PlaySound("./sound/part2.wav", winsound.SND_ASYNC)

def par2(event):

    canvas.create_image(0, 0, image=domaines, anchor="nw")
    image = Image.open('./Images/domaines.png')
    canvas.create_text(515, 100, text = "Piggy Adventure", fill="black", font=titre)
    canvas.create_text(515, 350, text = "La famille Cerdoza, une famille de digne cochons italiens, a pu survivre grâce à une grande\n fortune récolter grâce à des siècles de générations de circassiens et de trapézistes cochons. \n De nos jours, dans les baffons de la ville souterraine creusé depuis des millénaires, s’organise\n une rébellion. Principalement diriger par la famille Cerdoza qui grâce au pièce \n d’or réussit à manipuler les cupides Hommes, la grande révolte se déroulera dans trois jours. \n Cependant, la famille Cerdoza de par son pouvoir, effraie les Hommes au pouvoir. La police\n de la ferme, et l’escouade des abatteurs fait une descente chez les Cerdoza et \n perquisitionne leurs biens et leur domaine. Ils sont installés dans un cabanon non loin de la\n seul porte de PigCity, qui mène par le moyen d’un pont-levis au quartier général. Ou se trouve\n les postes de commandes qui contrôles le pont-levis, les armes technologiques des \n Hommes et les murailles qui entourent PigCity et les fermes où sont retenues les animaux. ", fill="#FFFFFF", tags="par3", font=recit)
    winsound.PlaySound("./sound/part3.wav", winsound.SND_ASYNC)

def par3(event):

    canvas.create_image( 0, 0, image = tunnels, anchor = "nw")
    image = Image.open('./Images/tunnels.png')
    canvas.create_text(515, 100, text = "Piggy Adventure", fill="white", font=titre)
    canvas.create_text(515, 350, text = "Le fils cadet de la famille Cerdoza, est de sang chaud. Il est incapable de\n garder ses convictions pour soi. Lors de la descente des autorités humaines, il ne peut\n s’empêcher, animé par la colère, de s’en prendre aux humains. Il est alors emmenés par les\n autorités au centre de détention des cochons coléreux. Entourés, dans la dernière voiture du\n convoi, par des gardes, il réussit à les assommer et à se faufiler dans les tuyaux du tunnel\n souterrain menant au quartier générales des hommes. Après avoir survécu pendant\n deux jours dans les souterrains chemianant à travers les conduit et les tuyaux de\n boues, il réussit à trouver le chemin vers les postes de contrôles. Il se trouve au-dessus d’une\n grande salle ronde au murs d’acier trempé blanc comme la neige. Du haut de son conduit, il\n aperçoit trois grandes portes de bois avec un garde posté à chacune d’elles. ‘nom du joueur’\n descends plonge dans la salle et abats les gardes-lards grâce à son agilité de circassiens. Il se\n trouve à présent au milieu de la salle, confronté au trois portes de bois massifs.", fill="#FFFFFF", tags="commencer", font=recit)
    winsound.PlaySound("./sound/part4.wav", winsound.SND_ASYNC)

def graphic():
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    canvas.create_text(515, 300, text="Piggy Adventure", fill="black", font=titre)

    canvas.create_rectangle(150, 500, 350, 600, fill="white", tags="histoire")
    canvas.create_text(250, 550, text = "Commencer", fill="black", font="consolas 30", tags="histoire")

    canvas.create_rectangle(650, 500, 850, 600, fill="white", tags="Tutoriel")
    canvas.create_text(750, 550, text = "Tutoriel", fill="black", font="consolas 30 ", tags="Tutoriel")


graphic()
canvas.tag_bind("Back", "<Button-1>", comeback)
canvas.tag_bind("exit", "<Button-1>", Exit)
canvas.tag_bind("par1", "<Button-1>", par1)
canvas.tag_bind("par2", "<Button-1>", par2)
canvas.tag_bind("par3", "<Button-1>", par3)
canvas.tag_bind("commencer", "<Button-1>", commencer)
canvas.tag_bind("Tutoriel", "<Button-1>", Tutoriel)
canvas.tag_bind("part1", "<Button-1>", part1)
canvas.tag_bind("part1a","<Button-1>,", part1a)
canvas.tag_bind("part2a","<Button-1>,", part2a)
canvas.tag_bind("part3a","<Button-1>,", part3a)
canvas.tag_bind("part4a","<Button-1>,", part4a)
canvas.tag_bind("part2", "<Button-1>", part2)
canvas.tag_bind("part3", "<Button-1>", part3)
canvas.tag_bind("part4", "<Button-1>", part4)
canvas.tag_bind("histoire", "<Button-1>", histoire)
canvas.tag_bind("ScenBack", "<Button-1>", ScenBack)
canvas.tag_bind("SetBack", "<Button-1>", SetBack)

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)

# Execute tkinter_____________________________________________________________________________________________________
root.mainloop()

