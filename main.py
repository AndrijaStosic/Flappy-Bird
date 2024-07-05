from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import random
import sys
import time

scoreboardd = 0

def padaj():
    global playerY, playerX, player, prozor, scoreboardd, scoreboard
    playerY += 2.5
    player.place(x=playerX, y=playerY)
    if playerY > 500:
        player.destroy()
        answer = messagebox.askyesno("Rip", "Da li želite da pokušate ponovo?")
        if answer:
            restart_game()
            scoreboardd = 0  
            scoreboard.config(text=scoreboardd)
        else:
            sys.exit()
    elif playerY < -30:
        player.destroy()
        answer = messagebox.askyesno("Rip", "Ne možete ići previše visoko. Pokušajte ponovo?")
        if answer:
            restart_game()
            scoreboardd = 0  
            scoreboard.config(text=scoreboardd)
        else:
            sys.exit()
    else:
        prozor.after(5, padaj)

def gore(event):
    global playerY, playerX, player
    playerY -= 100
    player.place(x=playerX, y=playerY)

def restart_game():
    global playerY, playerX, player, prozor, obstacle_passed
    playerX = 100
    playerY = 200
    player = Label(prozor, text="", height=2, width=5, bg="gold2")
    player.place(x=playerX, y=playerY)
    prozor.after(5, padaj)
    obstacle_passed = False

def kreci_prepreku():
    global preprekaX, preprekaY, prepreka
    preprekaY = random.randint(150, 500)  
    preprekaX = 488  
    prepreka = Label(prozor, text="", width=10, height=200, bg="lightgreen")
    prepreka.place(x=preprekaX, y=preprekaY)
    move_obstacle()

def move_obstacle():
    global preprekaX, preprekaY, prepreka, scoreboardd, scoreboard, obstacle_passed
    prepreka.place(x=preprekaX, y=preprekaY)
    preprekaX -= 1  
    if preprekaX < 20:
        prepreka.destroy()  
        kreci_prepreku()  
        obstacle_passed = False  
    else:
        prozor.after(2, move_obstacle)
    check_collision()
    if preprekaX < playerX and not obstacle_passed:
        scoreboardd += 1  
        scoreboard.config(text=scoreboardd)
        obstacle_passed = True

def check_collision():
    global playerX, playerY, preprekaX, preprekaY, prozor,scoreboard,scoreboardd
    if (preprekaX - 10 < playerX < preprekaX + 10) and (preprekaY - 20 < playerY < preprekaY + 200):
        player.destroy()
        time.sleep(0.1)
        playerX=40
        playerY=30
        answer = messagebox.askyesno("Rip", "Dodirnuli ste prepreku. Pokušajte ponovo?")
        scoreboardd=0
        scoreboard.config(text=scoreboardd)

        if answer:
            restart_game()
        else:
            sys.exit()




def stop():
    player.destroy()
    prepreka.destroy()


    



prozor = Tk()
prozor.geometry("488x600")
prozor.config(bg="lightblue")
prozor.title("Flappy Bird")
font = tkFont.Font(family="Fixedsys", size=30)

scoreboard = Label(prozor, text=scoreboardd, fg="Black", bg="lightblue", font=font)
scoreboard.pack()

playerX = 100
playerY = 200

player = Label(prozor, text="", height=2, width=5, bg="gold2")
player.place(x=playerX, y=playerY)


obstacle_passed = False

prozor.bind("<Button-1>", gore)

prozor.after(5, padaj)

kreci_prepreku()  

prozor.mainloop()
