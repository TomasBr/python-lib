import random


class block:
    o_block = [[[1, 1],
                [1, 1]]]
    block_types = [o_block]

    def __init__(self, x, y):
        self.rotation_index = 0
        self.block_type = self.block_types[0][0]
        self.x = int(x // 2) - int(len(self.block_type[0]) // 2)
        self.y = int(y)
