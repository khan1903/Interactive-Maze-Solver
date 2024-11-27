import pygame
import sys
from game_timer import Timer
from maze import Maze

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Maze Solver")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load the maze
#maze = Maze(r"D:\seeker_algo\upwork\interactive_maze_solver\src\assets\maze1.jpg", finish_area=(11, 0, 70, 476))  # Adjust finish area coordinates
maze = Maze(
    r"src\assets\maze1.jpg", 
    start_area=(1, 1, 70, 70),  # Define the start area
    finish_area=(1, 1, 70, 476)
)

# Timer
timer = Timer()

# Main game loop
running = True
solved = False
path_points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check collision
    # Check for collisions and update visited pixels
    if not maze.is_collision(mouse_x, mouse_y):
        maze.update_visited(mouse_x, mouse_y)

# Check if the game is completed
    if maze.is_completed(mouse_x, mouse_y):
        running = False
        xx=1
        print(f"You win! ")

    # Draw the maze
    screen.fill(WHITE)
    screen.blit(maze.maze_image, (0, 0))

    # Draw the path
    if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
        path_points.append((mouse_x, mouse_y))
    for point in path_points:
        pygame.draw.circle(screen, BLUE, point, 3)

    # Update the screen
    pygame.display.flip()

# Show win screen
if xx==1:
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, RED)
    time_taken = timer.get_elapsed_time()
    time_text = font.render(f"Time: {time_taken} seconds", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    pygame.time.wait(5000)

# Quit pygame
pygame.quit()
sys.exit()
