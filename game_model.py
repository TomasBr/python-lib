import pygame, shape


class game_model:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.landed_shapes = [[0 for col in range(self.cols)] for row in range(self.rows)]

    def update(self, landed_shape):
        for row in range(landed_shape.shape_height):
            for col in range(landed_shape.shape_width):
                if landed_shape.shape_type[row][col] != 0:
                    self.landed_shapes[row + landed_shape.y][col + landed_shape.x] = landed_shape.shape_type[row][col]
