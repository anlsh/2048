__author__ = 'Anish'

class Tile:

    def __init__(self, value, x, y, iteration):
        self.Size = value
        self.x = x
        self.y = y
        self.Iteration = iteration

class InvalidIndexError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class GarbageDump:

    #-1 is up
    def canVertical(self, tile, n):
        temp = 0
        try:
            temp = self.BoardArray[tile.x][tile.y + n]
        except BaseException:  #Should be OutOfBoundsError or something similar
            temp = self.NullTile

        return (tile.Iteration != self.iteration and \
                temp.Iteration != self.iteration and \
                tile.Size == temp.Size or \
                temp.Size == 0 and \
                tile.Size != 0)

#-1 is Left
    def canHorizontal(self, tile, n):
        temp = 0
        try:
            temp = self.BoardArray[tile.x + n][tile.y]
        except BaseException:  #Should be OutOfBoundsError or something similar
            temp = self.NullTile

        return (tile.Iteration != self.iteration and \
                temp.Iteration != self.iteration and \
                tile.Size == temp.Size or \
                temp.Size == 0 and \
                tile.Size != 0)

    def MoveHorizontal(self, dir):
        for x in range(self.Xsize)[::dir]:
            for y in range(self.Ysize):
                if self.canHorizontal(self.BoardArray[x][y], dir):
                    print("something should be moving")
                    self.BoardArray[x + dir][y] = \
                        Tile(self.BoardArray[x][y].Size + self.BoardArray[x + dir][y].Size, [x + dir, y],
                             self.iteration)
                    self.BoardArray[x][y] = Tile(0,[x,y],0)