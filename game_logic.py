"""This module contains all TETRIS logics"""

from constants import SHAPES
import random

class Tetris:
    """Do all operations of the tetromino and the grid"""

    def __init__(self):
        self.ROW = 20
        self.COL = 10
        self.grid = [[0 for _ in range(self.COL)] for _ in range(self.ROW)]
        self.curr_shape = self.pick_random_shape()
        self.next_shape = None

    def show(self):
        """Show the current grid"""

        return '\n'.join(' '.join(map(str, cell)) for cell in self.grid)

    def pick_random_shape(self):
        """Pick one shape randomly"""

        self.curr_shape = self.rotate_shape(SHAPES[random.randint(1, 7)])

    def rotate_shape(self, shape):
        """Change the orientation of the shape"""

        step = random.randint(1, 4)

        while step:
            step -= 1
            new_shape = [[0 for _ in range(3)] for _ in range(3)]

            for i in range(3):
                for j in reversed(range(3)):
                    new_shape[i][-j-1] = shape[j][i]
            shape = new_shape

        return shape
    
    def drop_shape(self, shape):
        """Drop the random shape on random col"""

        rand_col = random.randint(0, self.COL-3)

        # if the top row is all 0
        top = all(shape[0][j]==0 for j in range(3))

        # if the first column is all 0, we begin the loop for 1
        left = all(shape[j][0]==0 for j in range(3))

        # if the last column is all 0, we we terminate at 1
        right = all(shape[j][2]==0 for j in range(3))

        for i in range(top, 3):
            for j in range(left, 3-right):
                self.grid[i-top][j+rand_col] = shape[i][j]

    def play(self):
        """Play the game on console"""

        self.pick_random_shape()
        self.drop_shape(self.curr_shape)
        print(self.show())

if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()
