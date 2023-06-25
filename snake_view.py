import pygame

def draw_screen(screen, snake, food, score, score_x, score_y, font_size, font_name):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for segment in snake.segments:
        pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], snake.size, snake.size))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food.position[0], food.position[1], food.size, food.size))

    # Draw the score
    font = pygame.font.SysFont(font_name, font_size)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y))

def game_over(screen, score, score_x, score_y, font_size, font_name):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the game over text
    font = pygame.font.SysFont(font_name, font_size)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (score_x, score_y))

    # Draw the final score
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y + font_size))
