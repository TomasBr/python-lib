import random


class shape:
    O_SHAPE = [[[1, 1],
                [1, 1]]]
    J_SHAPE = [[[0, 2],
                [0, 2],
                [2, 2]],
               [[2, 0, 0],
                [2, 2, 2]],
               [[2, 2],
                [2, 0],
                [2, 0]],
               [[2, 2, 2],
                [0, 0, 2]]]
    L_SHAPE = [[[3, 0],
                [3, 0],
                [3, 3]],
               [[3, 3, 3],
                [3, 0, 0]],
               [[3, 3],
                [0, 3],
                [0, 3]],
               [[0, 0, 3],
                [3, 3, 3]]]
    T_SHAPE = [[[4, 4, 4],
                [0, 4, 0]],
               [[0, 4],
                [4, 4],
                [0, 4]],
               [[0, 4, 0],
                [4, 4, 4]],
               [[4, 0],
                [4, 4],
                [4, 0]]]

    S_SHAPE = [[[0, 5, 5],
                [5, 5, 0]],
               [[5, 0],
                [5, 5],
                [0, 5]]]

    Z_SHAPE = [[[6, 6, 0],
                [0, 6, 6]],
               [[0, 6],
                [6, 6],
                [6, 0]]]

    I_SHAPE = [[[0, 7, 0, 0],
                [0, 7, 0, 0],
                [0, 7, 0, 0],
                [0, 7, 0, 0]],
               [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [7, 7, 7, 7],
                [0, 0, 0, 0]]]

    SHAPE_TYPES = [O_SHAPE, J_SHAPE, L_SHAPE, T_SHAPE, S_SHAPE, Z_SHAPE, I_SHAPE]

    def __init__(self, x, y):
        self.rotation_index = 0
        self.shape_types = random.choice(self.SHAPE_TYPES)
        self.shape_type = self.shape_types[self.rotation_index]
        self.shape_width = len(self.shape_type[0])
        self.shape_height = len(self.shape_type)
        self.x = int(x // 2) - int(len(self.shape_type[0]) // 2)
        self.y = int(y)

    def rotate90(self):
        self.rotation_index = (self.rotation_index + 1) % len(self.shape_types)
        self.shape_type = self.shape_types[self.rotation_index]
        self.shape_width = len(self.shape_type[0])
        self.shape_height = len(self.shape_type)
        return self
