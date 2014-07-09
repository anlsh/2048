__author__ = 'Anish'

import pyglet
from pyglet.window import key
from pyglet.gl import *

from Board import Board

class Frontend(pyglet.window.Window):

    def __init__(self, GameX, GameY, Wx=512, Wy=512):
        super().__init__(width=Wx, height=Wy, visible=True)
        self.GameX = GameX
        self.GameY = GameY
        self.Wx = Wx
        self.Wy = Wy

        #pyglet.clock.schedule_interval(self.update, 1/60.0)

        self.font = pyglet.font.load("Helvetica", Wx/16)

        self.GameInstance = Board(GameX, GameY)
        self.GameInstance.BoardArray = self.GameInstance.SpawnATile(self.GameInstance.BoardArray)

        #pyglet.clock.schedule_interval(self.GameInstance.PrintBoard(self.GameInstance.BoardArray), 5)
        #THE ABOVE LINE CAUSES CREASHES- WHY?

    def update(self, dt):
        self.on_draw()
        if self.GameInstance.GameOver(self.GameInstance.BoardArray):
            self.close()

    def TextMode(self):
        while not self.GameInstance.GameOver(self.GameInstance.BoardArray):
            self.GameInstance.BoardArray = self.GameInstance.SpawnATile(self.GameInstance.BoardArray)
            self.GameInstance.PrintBoard(self.GameInstance.BoardArray)

            n = input("Move?")
            while n not in ["up", "down", "left", "right"] or self.GameInstance.BoardArray \
                    == self.GameInstance.Move(n, self.GameInstance.BoardArray):
                n = input("Invalid move, pick again")

            self.GameInstance.Move(n, self.GameInstance.BoardArray)

        print("Game Over!")

    def on_draw(self):
        self.clear()
        for x in range(self.GameX)[::1]:
            for y in range(self.GameY):
                self.draw_tile(y, x, self.GameInstance.BoardArray[x][y])

    def draw_square(self, x, y, Xsize=128, Ysize=128, c=[255,255,255]):
        glBegin(GL_POLYGON)
        glColor3f(c[0], c[1], c[2])
        glVertex2f(x,y)
        glVertex2f(x+Xsize,y)
        glVertex2f(x+Xsize,y+Ysize)
        glVertex2f(x, y+Ysize)
        glEnd()

    def draw_tile(self, x, y, size):
        dx = self.Wx/self.GameX
        dy = self.Wy/self.GameY
        self.draw_square(x*dx, self.Wy - self.Wy/self.GameY - y*dy, dx, dy)
        self.draw_square(x*dx+6, self.Wy - self.Wy/self.GameY - y*dy + 6, dx-12, dy-12, [0,0,0])

        text = pyglet.font.Text(
            self.font,
            size.__str__(),
            x=x*dx + dx/2,
            y= self.Wy -(y*dy + dy/2),
            halign=pyglet.font.Text.CENTER,
            valign=pyglet.font.Text.CENTER,
            color=(1, 1, 1, 0.5),
        )
        text.draw()

    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)

        if symbol == key.A or symbol == key.LEFT:
            if self.GameInstance.Move("left", self.GameInstance.BoardArray) \
                    != self.GameInstance.BoardArray:
                self.GameInstance.BoardArray = self.GameInstance.iterate("left", self.GameInstance.BoardArray)
        if symbol == key.D or symbol == key.RIGHT:
            if self.GameInstance.Move("right", self.GameInstance.BoardArray) \
                    != self.GameInstance.BoardArray:
                self.GameInstance.BoardArray = self.GameInstance.iterate("right", self.GameInstance.BoardArray)
        if symbol == key.W or symbol == key.UP:
            if self.GameInstance.Move("up", self.GameInstance.BoardArray) \
                    != self.GameInstance.BoardArray:
                self.GameInstance.BoardArray = self.GameInstance.iterate("up", self.GameInstance.BoardArray)
        if symbol == key.D or symbol == key.DOWN:
            if self.GameInstance.Move("down", self.GameInstance.BoardArray) \
                    != self.GameInstance.BoardArray:
                self.GameInstance.BoardArray = self.GameInstance.iterate("down", self.GameInstance.BoardArray)

if __name__ == "__main__":
    f = Frontend(4,4)
    pyglet.app.run()
