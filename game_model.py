import pygame


class game_model:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.landed_shapes = [[0 for x in range(self.height)] for y in range(self.width)]

    def update(self, landed_shape):
        for x in range(landed_shape.shape_width):
            for y in range(landed_shape.shape_height):
                self.landed_shapes[x + landed_shape.x][y + landed_shape.y] = 1
