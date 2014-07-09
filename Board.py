__author__ = 'Anish'

import random
from copy import copy, deepcopy

class Board:

    def __init__(self, xsize, ysize):
        self.iteration = 0
        self.Xsize = xsize
        self.Ysize = ysize

        self.BoardArray = []
        self.InitArray = []

        for y in range(self.Xsize):
            for x in range(self.Ysize):
                self.InitArray.append(0)
            self.BoardArray.append(self.InitArray)
            self.InitArray = []

    def PrintBoard(self, PrintArray):
        print("\n", end="")
        for x in range(self.Xsize):
            print("[ ", end="")
            for y in range(self.Ysize):
                print(PrintArray[x][y], end=" ")
            print("]")
            print("")

    def EmptyTileList(self, CheckArray):
        ETL = []
        for x in range(0, self.Xsize):
            for y in range(0, self.Ysize):
                if CheckArray[x][y] == 0:
                    ETL.append([x,y])
        return ETL

    def SpawnATile(self, SpawnArray_):

        SpawnArray = deepcopy(SpawnArray_)
        ETL = self.EmptyTileList(SpawnArray)

        #if ETL != []:
            #print("Tiles remaining to fill: "+len(ETL).__str__())
            #for e in ETL:
                #print("("+e[0].__str__() + ", "+e[1].__str__()+")")
        #else:
            #print("Done")

        try:
            t = random.choice(ETL)
            #print("CHOOSING "+t[0].__str__() + ", "+t[1].__str__()+" TO COVERT")
        except IndexError:
            return None

        SpawnArray[t[0]][t[1]] = 2

        ETL = t = None

        return SpawnArray

    def MainLoop(self):
        for x in range(16):
            self.iteration += 1
            print("ITERATION: "+x.__str__())
            self.PrintBoard(self.BoardArray)
            self.BoardArray = self.SpawnATile(self.BoardArray)
            print("-------------------------------------------")

        self.PrintBoard(self.BoardArray)

        print("SOMETHING")

        self.BoardArray = self.Move(input("Move Direction?"), self.BoardArray)

        self.PrintBoard(self.BoardArray)

    def Vertical(self, dir, GivenArray_):

        if dir == "up":
            dir = 1
        elif dir == "down":
            dir = -1

        GivenArray = deepcopy(GivenArray_)
        #-1 down
        #1 up
        for y in range(self.Ysize):
            TempArray = []
            for x1 in range(self.Xsize):
                TempArray.append(GivenArray[x1][y])

            FinArray = self.collapse(TempArray, dir)

            for x2 in range(self.Xsize):
                GivenArray[x2][y] = FinArray[x2]

        return GivenArray

    def Horizontal(self, dir, GivenArray_):

        if dir == "left":
            dir = 1
        elif dir == "right":
            dir = -1

        GivenArray = deepcopy(GivenArray_)
        #-1 right
        #1 left
        for x in range(self.Xsize):
            TempArray = []
            for y1 in range(self.Ysize):
                TempArray.append(GivenArray[x][y1])

            FinArray = self.collapse(TempArray, dir)

            for y2 in range(self.Ysize):
                GivenArray[x][y2] = FinArray[y2]

        return GivenArray

    def Move(self, dir, GivenArray):
        if dir == "up" or dir == "down":
            return self.Vertical(dir, GivenArray)
        elif dir == "left" or dir == "right":
            return self.Horizontal(dir, GivenArray)
        else:
            return self.BoardArray

    def GameOver(self, DeathArray):
        h1 = DeathArray == self.Horizontal(1, DeathArray)
        v1 = DeathArray == self.Vertical(1, DeathArray)
        h2 = DeathArray == self.Horizontal(-1, DeathArray)
        v2 = DeathArray == self.Vertical(-1, DeathArray)
        t = len(self.EmptyTileList(DeathArray)) != 16
        return (h1 and h2 and v1 and v2 and t)

    def collapse(self, array, dir):
        ZeroArray =[]
        for u in range(len(array)-1):
            ZeroArray.append(0)
        if array == ZeroArray:
            return ZeroArray

        Squashed = array[::dir]

        for x in range(len(Squashed)):
            try:
                Squashed.remove(0)
            except ValueError:
                break

        for x in range(len(Squashed)):
            try:
                if Squashed[x] == Squashed[x+1]:
                    Squashed[x] = 2*Squashed[x]
                    Squashed.pop(x+1)
            except IndexError:
                pass

        for x in range(4):
            Squashed.append(0)
        Squashed = Squashed[:4]
        return Squashed[::dir]

    def iterate(self, dir, GameArray):
        GameArray = deepcopy(GameArray)
        GameArray = self.Move(dir, GameArray)
        GameArray = self.SpawnATile(GameArray)

        return GameArray