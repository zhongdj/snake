import pygame
from snake_model import Snake, Food, Game
from snake_view import draw_screen, game_over
from snake_controller import handle_input

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 10
SNAKE_START_LENGTH = 5
SNAKE_START_X = SCREEN_WIDTH // 2
SNAKE_START_Y = SCREEN_HEIGHT // 2
FOOD_SIZE = 10
SCORE_X = 20
SCORE_Y = 20
FONT_SIZE = 30
FONT_NAME = "Arial"

def main():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    # Set up the clock
    clock = pygame.time.Clock()

    # Create the game objects
    snake = Snake(SNAKE_START_X, SNAKE_START_Y, SNAKE_SIZE, SNAKE_START_LENGTH)
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_SIZE)
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, SCORE_X, SCORE_Y, FONT_SIZE, FONT_NAME)

    # Start the game loop
    game.start()
    while game.running:
        # Handle input
        handle_input(snake)

        # Update game state
        snake.move()
        if snake.check_collision(SCREEN_WIDTH, SCREEN_HEIGHT):
            game.end()
            continue
        if snake.segments[0] == food.position:
            snake.grow()
            food.place()
            game.update_score()
        draw_screen(screen, snake, food, game.score, SCORE_X, SCORE_Y, FONT_SIZE, FONT_NAME)

        # Update the screen
        pygame.display.update()
        pygame.display.flip()

        # Tick the clock
        clock.tick(10)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
