import random

class shape:
    O_SHAPE = [[[1, 1],
                [1, 1]]]
    SHAPE_TYPES = [O_SHAPE]

    def __init__(self, x, y):
        self.rotation_index = 0
        self.shape_type = self.SHAPE_TYPES[0][0]
        self.shape_width = len(self.shape_type[0])
        self.shape_height = len(self.shape_type)
        self.x = int(x // 2) - int(len(self.shape_type[0]) // 2)
        self.y = int(y)
