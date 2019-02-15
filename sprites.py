import tkinter
import random
import time

class Board(object):
    def __init__(self, window):
        self.window = window
        self.canvas = tkinter.Canvas(self.window, width=500, height=700, background="#4EC0CA", bd=0, highlightthickness=0)
        self.canvas.pack()

        self.bird = Bird(self.canvas, "images/bird.gif", g=5)

        self.window.bind("<space>", self.bird.up)

        self.pipes = list()
        self.pipes.append(Pipe(self.canvas, y=random.randint(50, 650), speed=5))

        self.score_text = self.canvas.create_text(20, 20, text=str(self.bird.score), font='Impact 20', fill="#ff0000")

    def update(self):
        if not self.bird.dead:
            if self.pipes[0].x[1] < 0:
                del self.pipes[0]

            if self.pipes[0].x[1] == 200:
                self.pipes.append(Pipe(self.canvas, y=random.randint(50, 650), speed=5))

            for pipe in self.pipes:
                pipe.update()

            if self.bird.x > self.pipes[0].x[0] and self.bird.x < self.pipes[0].x[1]:
                self.bird.detectCollision(self.pipes[0])

            if self.bird.x == self.pipes[0].x[0]:
                self.bird.score += 1
                self.canvas.itemconfig(self.score_text, text=str(self.bird.score))

            self.bird.update()

            self.window.after(4, self.update)

        else:
            self._game_over()

    def _game_over(self):

        self.canvas["bg"] = "black"

        for pipe in self.pipes:
            pipe.hide()

        self.bird.hide()
        del self.bird

        self.canvas.delete(self.score_text)

        self.lose_text = list()
        self.lose_text.append(self.canvas.create_text(250, 150, text="HECK YOU", font='Impact 60', fill='#ff0000', anchor=tkinter.CENTER))
        self.lose_text.append(self.canvas.create_text(250, 350, text="PRESS SPACE", font='Impact 60', fill='#ff0000', anchor=tkinter.CENTER))
        self.lose_text.append(self.canvas.create_text(250, 450, text="TO RESTART", font='Impact 60', fill='#ff0000', anchor=tkinter.CENTER))

        self.window.unbind("<space>")
        self.window.bind("<space>", self.restart)

    def restart(self, event=None):
        self.window.unbind("<space")
        self.canvas["bg"] = "#4EC0CA"

        self.bird = Bird(self.canvas, "images/bird.gif", g=5)

        for line in self.lose_text:
            self.canvas.delete(line)

        self.pipes = list()
        self.pipes.append(Pipe(self.canvas, y=random.randint(50, 650), speed=5))

        self.score_text = self.canvas.create_text(20, 20, text=str(self.bird.score), font='Impact 20', fill="#ff0000")

        self.window.bind("<space>", self.bird.up)
        self.update()

class Bird(object):
    def __init__(self, canvas, img_path, g=5, x=100, y=300):
        self.score = 0
        self.img = tkinter.PhotoImage(file=img_path)
        self.g = g
        self.x = x
        self.y = y
        self.canvas = canvas
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)
        self.dead = False

    def _down(self):
        # fix
        self.y += self.g
        self.canvas.delete(self.sprite)
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)

    def kill(self):
        self.dead = True

    def update(self):
        if self.y > 675 or self.y < 0:
            self.kill()
        self._down()

    def up(self, event=None):
        self.y -= self.g * 25
        self.canvas.delete(self.sprite)
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)

    def hide(self):
        self.canvas.delete(self.sprite)

    def show(self):
        pass
        #self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)

    def detectCollision(self, pipe):
        if not (self.y > pipe.y - 150 and self.y < pipe.y + 150):
            self.dead = True

class Pipe(object):
    def __init__(self, canvas, speed=5, x=550, y=350, thickness=50, hole_size=300):
        self.speed = speed
        self.x = [x - thickness, x]
        self.y = y
        self.canvas = canvas
        self.thickness = thickness
        self.hole_size = hole_size
        #outline argument prevents black outline default
        self.top = self.canvas.create_rectangle(self.x[0], 0, self.x[1], self.y - self.hole_size / 2, fill="#74BF2E", outline="#74BF2E")
        self.bottom = self.canvas.create_rectangle(self.x[0], 700, self.x[1], self.y + self.hole_size / 2, fill="#74BF2E", outline="#74BF2E")

    def update(self):
        self.x = [self.x[0] - self.speed, self.x[1] - self.speed]
        self.canvas.coords(self.top, self.x[0], 0, self.x[1], self.y - self.hole_size / 2)
        self.canvas.coords(self.bottom, self.x[0], 700, self.x[1], self.y + self.hole_size / 2)

    def hide(self):
        self.canvas.delete(self.top)
        self.canvas.delete(self.bottom)
