# Import and initialize the pygame library
import pygame, time, shape, game_model

from shape import shape
from game_model import game_model

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (237, 11, 25)
LIGHTBLUE = (41, 240, 239)
DARKBLUE = (10, 33, 236)
ORANGE = (238, 101, 38)
YELLOW = (246, 238, 52)
GREEN = (38, 238, 43)
PURPLE = (159, 35, 236)

FPS = 60
CAPTION_FONT_NAME = "comicsans"
CAPTION_FONT_SIZE = 60

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAY_WIDTH = 200  # meaning 200 // 10 = 20 width per block
PLAY_HEIGHT = 400  # meaning 400 // 20 = 20 height per block
BLOCK_SIZE = 20
BOARD_WIDTH = int(PLAY_WIDTH / BLOCK_SIZE)
BOARD_HEIGHT = int(PLAY_HEIGHT / BLOCK_SIZE)
TOP_LEFT_X = (SCREEN_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = SCREEN_HEIGHT - PLAY_HEIGHT - 10


def main():
    global screen, clock, caption_font, caption_label
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    caption_font = pygame.font.SysFont(CAPTION_FONT_NAME, CAPTION_FONT_SIZE)
    caption_label = make_text_object("TETRIS", caption_font, WHITE)

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
    model = game_model(BOARD_HEIGHT, BOARD_WIDTH)  # 20 rows and 10 columns

    # Run until the user asks to quit
    running = True
    fall_speed = 0.5
    last_fall_time = time.time()

    falling_shape = get_new_shape()
    while running:
        if falling_shape is None:
            falling_shape = get_new_shape()
            last_fall_time = time.time()
            if not is_valid_position(model, falling_shape, adj_y=1):
                return

        # Handle user keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and is_valid_position(model, falling_shape, adj_x=-1):
                    falling_shape.x -= 1
                elif event.key == pygame.K_RIGHT and is_valid_position(model, falling_shape, adj_x=1):
                    falling_shape.x += 1
                elif event.key == pygame.K_UP:
                    falling_shape = falling_shape.rotate90()
                elif event.key == pygame.K_DOWN and is_valid_position(model, falling_shape, adj_y=1):
                    falling_shape.y += 1
                    last_fall_time = time.time()
                elif event.key == pygame.K_SPACE:
                    for y in range(1, BOARD_HEIGHT):
                        if not is_valid_position(model, falling_shape, adj_y=y):
                            break
                    falling_shape.y += y - 1

        now = time.time()
        if now - last_fall_time >= fall_speed:
            last_fall_time = now
            if is_valid_position(model, falling_shape, adj_y=1):
                falling_shape.y += 1
            else:
                model.update(falling_shape)
                falling_shape = None

        draw_board(model)
        if falling_shape is not None:
            draw_shape(falling_shape)

        # Update the display
        pygame.display.update()
        clock.tick(FPS)
    # Done! Time to quit.
    pygame.quit()


def is_on_board(x, y):
    return 0 <= x < BOARD_WIDTH and y < BOARD_HEIGHT


def is_valid_position(model, shape, adj_x=0, adj_y=0):
    for row in range(shape.shape_height):
        for col in range(shape.shape_width):
            if shape.shape_type[row][col] != 0:
                if not is_on_board(col + shape.x + adj_x, row + shape.y + adj_y):
                    return False
                if model.landed_shapes[row + shape.y + adj_y][col + shape.x + adj_x] != 0:
                    return False
    return True


def draw_board(model):
    screen.fill(BLACK)
    screen.blit(caption_label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (caption_label.get_width() / 2), 25))
    pygame.draw.rect(screen, (94, 18, 36), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 5)

    for row in range(model.rows):
        for col in range(model.cols):
            if model.landed_shapes[row][col] != 0:
                pixel_x, pixel_y = convert_to_pixel_coords(col, row)
                draw_box(pixel_x, pixel_y, get_color_from_index(model.landed_shapes[row][col]))


def get_new_shape():
    return shape(BOARD_WIDTH, -1)


def draw_shape(shape):
    pixel_x, pixel_y = convert_to_pixel_coords(shape.x, shape.y)
    for row in range(shape.shape_height):
        for col in range(shape.shape_width):
            if shape.shape_type[row][col] != 0:
                draw_box(pixel_x + (col * BLOCK_SIZE), pixel_y + (row * BLOCK_SIZE), get_color_from_index(shape.shape_type[row][col]))


def draw_box(pixel_x, pixel_y, color):
    pygame.draw.rect(screen, color, (pixel_x + 1, pixel_y + 1, BLOCK_SIZE - 1, BLOCK_SIZE - 1))


def convert_to_pixel_coords(box_x, box_y):
    return TOP_LEFT_X + (box_x * BLOCK_SIZE), TOP_LEFT_Y + (box_y * BLOCK_SIZE)


def make_text_object(text, font, color):
    return font.render(text, True, color)


def get_color_from_index(index):
    color_dict = {
        1: YELLOW,
        2: DARKBLUE,
        3: ORANGE,
        4: LIGHTBLUE,
        5: GREEN,
        6: RED,
        7: PURPLE
    }
    return color_dict.get(index)


if __name__ == "__main__":
    main()
