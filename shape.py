import random


class shape:
    O_SHAPE = [[[1, 1],
                [1, 1]]]
    J_SHAPE = [[[0, 1],
                [0, 1],
                [1, 1]],
               [[1, 0, 0],
                [1, 1, 1]],
               [[1, 1],
                [1, 0],
                [1, 0]],
               [[1, 1, 1],
                [0, 0, 1]]]
    L_SHAPE = [[[1, 0],
                [1, 0],
                [1, 1]],
               [[1, 1, 1],
                [1, 0, 0]],
               [[1, 1],
                [0, 1],
                [0, 1]],
               [[0, 0, 1],
                [1, 1, 1]]]
    T_SHAPE = [[[1, 1, 1],
                [0, 1, 0]],
               [[0, 0, 1],
                [0, 1, 1],
                [0, 0, 1]],
               [[0, 1, 0],
                [1, 1, 1]],
               [[1, 0, 0],
                [1, 1, 0],
                [1, 0, 0]]]

    SHAPE_TYPES = [O_SHAPE, J_SHAPE, L_SHAPE, T_SHAPE]

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
