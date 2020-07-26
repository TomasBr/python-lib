# Import and initialize the pygame library
import pygame, time, shape, game_model

from shape import shape
from game_model import game_model

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
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

    model = game_model(BOARD_WIDTH, BOARD_HEIGHT)

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
                    print("Up arrow")
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
    for x in range(shape.shape_width):
        for y in range(shape.shape_height):
            if not is_on_board(x + shape.x + adj_x, y + shape.y + adj_y):
                return False
            if model.landed_shapes[x + shape.x + adj_x][y + shape.y + adj_y] != 0:
                return False
    return True


def draw_board(model):
    screen.fill(BLACK)
    screen.blit(caption_label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (caption_label.get_width() / 2), 25))
    pygame.draw.rect(screen, (94, 18, 36), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 5)

    for x in range(model.width):
        for y in range(model.height):
            if model.landed_shapes[x][y] != 0:
                pixel_x, pixel_y = convert_to_pixel_coords(x, y)
                draw_box(pixel_x, pixel_y)


def get_new_shape():
    return shape(BOARD_WIDTH, -1)


def draw_shape(shape):
    pixel_x, pixel_y = convert_to_pixel_coords(shape.x, shape.y)
    for x in range(shape.shape_width):
        for y in range(shape.shape_height):
            draw_box(pixel_x + (x * BLOCK_SIZE), pixel_y + (y * BLOCK_SIZE))


def draw_box(pixel_x, pixel_y):
    pygame.draw.rect(screen, RED, (pixel_x + 1, pixel_y + 1, BLOCK_SIZE - 1, BLOCK_SIZE - 1))


def convert_to_pixel_coords(box_x, box_y):
    return TOP_LEFT_X + (box_x * BLOCK_SIZE), TOP_LEFT_Y + (box_y * BLOCK_SIZE)


def make_text_object(text, font, color):
    return font.render(text, True, color)


if __name__ == "__main__":
    main()
