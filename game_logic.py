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

    def show(self, grid):
        """Show the current grid"""

        return '\n'.join(''.join(map(str, cell)) for cell in grid)

    def pick_random_shape(self):
        """Pick one shape randomly"""

        return self.rotate_shape(SHAPES[random.randint(1, 7)])

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

    def play(self):
        """Play the game on console"""

        print(self.show(self.pick_random_shape()))

if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()
