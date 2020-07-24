import pygame


class game_model:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.landed_blocks = [[0 for x in range(self.height)] for y in range(self.width)]

    def update(self, landed_block):
        for x in range(len(landed_block.block_type[0])):
            for y in range(len(landed_block.block_type)):
                self.landed_blocks[x + landed_block.x][y + landed_block.y] = 1
