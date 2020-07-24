# Import and initialize the pygame library
import pygame, time, block, game_model
from pygame.locals import *
from block import block
from game_model import game_model

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
CAPTION_FONT_NAME = "comicsans"
CAPTION_FONT_SIZE = 60

s_width = 640
s_height = 480
play_width = 200  # meaning 200 // 10 = 20 width per block
play_height = 400  # meaning 400 // 20 = 20 height per block
block_size = 20
board_width = int(play_width / block_size)
board_height = int(play_height / block_size)
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height - 10


def main():
    global screen, clock, caption_font
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([s_width, s_height])
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    caption_font = pygame.font.SysFont(CAPTION_FONT_NAME, CAPTION_FONT_SIZE)
    run_game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
    pygame.quit()

def run_game():
    """ game entry point """
    global caption_label

    caption_label = make_text_object("TETRIS", caption_font, WHITE)
    model = game_model(board_width, board_height)

    # Run until the user asks to quit
    running = True
    fall_speed = 0.5
    last_fall_time = time.time()

    falling_block = get_new_block()
    while running:
        if falling_block is None:
            falling_block = get_new_block()
            last_fall_time = time.time()
            if not is_valid_position(model, falling_block, adj_y=1):
                return

        # Handle user keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and is_valid_position(model, falling_block, adj_x=-1):
                    falling_block.x -= 1
                elif event.key == pygame.K_RIGHT and is_valid_position(model, falling_block, adj_x=1):
                    falling_block.x += 1
                elif event.key == pygame.K_UP:
                    print("Up arrow")
                elif event.key == pygame.K_DOWN and is_valid_position(model, falling_block, adj_y=1):
                    falling_block.y += 1
                    last_fall_time = time.time()
                elif event.key == pygame.K_SPACE:
                    for y in range(1, board_height):
                        if not is_valid_position(model, falling_block, adj_y=y):
                            break
                    falling_block.y += y - 1

        now = time.time()
        if now - last_fall_time >= fall_speed:
            last_fall_time = now
            if is_valid_position(model, falling_block, adj_y=1):
                falling_block.y += 1
            else:
                model.update(falling_block)
                falling_block = None

        draw_board(model)
        if falling_block is not None:
            draw_block(falling_block)

        # Update the display
        pygame.display.update()
        clock.tick(FPS)
    # Done! Time to quit.
    pygame.quit()


def is_on_board(x, y):
    return 0 <= x < board_width and y < board_height


def is_valid_position(model, block, adj_x=0, adj_y=0):
    for x in range(len(block.block_type[0])):
        for y in range(len(block.block_type)):
            if not is_on_board(x + block.x + adj_x, y + block.y + adj_y):
                return False
            if model.landed_blocks[x + block.x + adj_x][y + block.y + adj_y] != 0:
                return False
    return True


def draw_board(model):
    screen.fill(BLACK)
    screen.blit(caption_label, (top_left_x + play_width / 2 - (caption_label.get_width() / 2), 25))
    pygame.draw.rect(screen, (94, 18, 36), (top_left_x, top_left_y, play_width, play_height), 5)

    for x in range(model.width):
        for y in range(model.height):
            if model.landed_blocks[x][y] != 0:
                pixel_x, pixel_y = convert_to_pixel_coords(x, y)
                draw_box(pixel_x, pixel_y)


def draw_block(block):
    pixel_x, pixel_y = convert_to_pixel_coords(block.x, block.y)
    for x in range(len(block.block_type[0])):
        for y in range(len(block.block_type)):
            draw_box(pixel_x + (x * block_size), pixel_y + (y * block_size))


def draw_box(pixel_x, pixel_y):
    pygame.draw.rect(screen, RED, (pixel_x + 1, pixel_y + 1, block_size - 1, block_size - 1))


def convert_to_pixel_coords(box_x, box_y):
    return top_left_x + (box_x * block_size), top_left_y + (box_y * block_size)


def get_new_block():
    return block(board_width, -1)


def make_text_object(text, font, color):
    return font.render(text, True, color)


if __name__ == "__main__":
    main()
