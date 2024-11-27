import pygame
import time
class Timer:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()

    def get_elapsed_time(self):
        """Returns the time elapsed in seconds."""
        current_time = pygame.time.get_ticks()
        return (current_time - self.start_time) // 1000

    def reset(self):
        """Resets the timer."""
        self.start_time = pygame.time.get_ticks()
    

