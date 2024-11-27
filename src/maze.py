import pygame

class Maze:
    def __init__(self, maze_image_path, start_area, finish_area):
        self.maze_image = pygame.image.load(maze_image_path).convert()
        self.obstacle_color = (0, 0, 0)  # Color for obstacles
        self.path_color = (255, 255, 255)  # Color for valid path
        self.start_area = pygame.Rect(start_area)  # Define the start area
        self.finish_area = pygame.Rect(finish_area)  # Define the finish area
        self.visited = set()  # Keep track of visited pixels
        self.started = False  # Track if the player has started

    def draw(self, screen):
        """Draws the maze on the screen."""
        screen.blit(self.maze_image, (0, 0))


    def is_collision(self, x, y):
        # Ensure coordinates are within maze bounds
        if 0 <= x < self.maze_image.get_width() and 0 <= y < self.maze_image.get_height():
            pixel_color = self.maze_image.get_at((x, y))
            return pixel_color == self.obstacle_color
        return False  # Out of bounds is not a collision

    def is_on_path(self, x, y):
        # Check if the current position is on the valid path
        if 0 <= x < self.maze_image.get_width() and 0 <= y < self.maze_image.get_height():
            pixel_color = self.maze_image.get_at((x, y))
            return pixel_color == self.path_color
        return False

    def is_completed(self, x, y):
        # Check if the player is in the finish area after following the path
        return self.started and self.finish_area.collidepoint(x, y) and len(self.visited) > 100  # Adjust required path length

    def update_visited(self, x, y):
        # Update visited pixels if on the path
        if self.is_on_path(x, y):
            self.visited.add((x, y))
            if self.start_area.collidepoint(x, y):
                self.started = True  # Player has started the maze

