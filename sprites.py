import tkinter

class Bird(object):
    def __init__(self, canvas, img, speed=5, x=100, y=300):
        self.img = img
        self.speed = speed
        self.x = x
        self.y = y
        self.canvas = canvas
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)
        self.dead = False

    def _down(self):
        self.y += self.speed
        self.canvas.delete(self.sprite)
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)

    def kill(self):
        self.dead = True

    def update(self):
        #if self.y < 675:
            #self.kill()
        self._down()
    
    def hide(self):
        self.canvas.delete(self.sprite)
    
    def up(self, event=None):
        self.y -= 50
        self.canvas.delete(self.sprite)
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.img)

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
        self.x = [self.x[0] - 1, self.x[1] - 1]
        self.canvas.coords(self.top, self.x[0], 0, self.x[1], self.y - self.hole_size / 2)
        self.canvas.coords(self.bottom, self.x[0], 700, self.x[1], self.y + self.hole_size / 2)\

    def hide(self):
        self.canvas.delete(self.top)
        self.canvas.delete(self.bottom)
