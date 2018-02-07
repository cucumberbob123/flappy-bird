import tkinter
import random
import os
import time
from sprites import Board, Bird, Pipe

FRAMERATE = 60

main = tkinter.Tk()

main.resizable(width = False, height = False)

main.title("Flappy Bird")

main.geometry('500x700')

main.tk.call('wm', 'iconphoto', main._w, tkinter.PhotoImage(file="images/bird.gif"))


board = Board(main)
board.update()

main.mainloop()
