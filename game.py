import tkinter
import random
import os
import time
from sprites import Bird, Pipe

FRAMERATE = 60
SCORE = 0

def game_over():
    print("You bad!")

main = tkinter.Tk()

main.resizable(width = False, height = False)

main.title("Flappy Bird")

main.geometry('500x700')

BIRD_IMG = tkinter.PhotoImage(file="images/bird.gif")
main.tk.call('wm', 'iconphoto', main._w, BIRD_IMG)

canvas = tkinter.Canvas(main, width=500, height=700, background="#4EC0CA", bd=0, highlightthickness=0)
canvas.pack()

bird = Bird(canvas, BIRD_IMG, speed=1)

pipes = list()
pipes.append(Pipe(canvas, x=250, y=random.randint(50, 650), speed=1))
pipes.append(Pipe(canvas, y=random.randint(50, 650), speed=1))

def update_all():
    if not bird.dead():
        if pipes[0].x[1] < 0:
            del pipes[0]
            pipes.append(Pipe(canvas, y=random.randint(50, 650), speed=1))

        for pipe in pipes:
            pipe.update()

        bird.update()

        main.after(FRAMERATE // 15, update_all)
    else:
        canvas["bg"] = "black"

        for pipe in pipes:
            pipe.hide()
        bird.hide()

        canvas.create_text(250, 350, text="YOU LOSE", font='Impact 60', fill='#ff0000', anchor=tkinter.CENTER)
        main.unbind("<space>")

update_all()
main.bind("<space>", bird.up)
main.mainloop()
