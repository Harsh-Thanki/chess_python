# Square.py

import pygame

# Tile creator
class Square:
    def __init__(self, x, y, width, height):
        self.x = x  # x-coordinate of the square in the grid
        self.y = y  # y-coordinate of the square in the grid
        self.width = width  # Width of the square
        self.height = height  # Height of the square
        self.abs_x = x * width  # Absolute x-coordinate based on grid position
        self.abs_y = y * height  # Absolute y-coordinate based on grid position
        self.abs_pos = (self.abs_x, self.abs_y)  # Absolute position tuple
        self.pos = (x, y)  # Position tuple (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'  # Color of the square based on its position
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)  # Color for drawing the square
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)  # Color for highlighting the square
        self.occupying_piece = None  # The chess piece occupying the square (if any)
        self.coord = self.get_coord()  # Formal notation of the square (e.g., 'a1', 'b2', etc.)
        self.highlight = False  # Flag indicating whether the square should be highlighted
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )  # Pygame rectangle representing the square's position and size

    # Get the formal notation of the tile
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        # Configures if the tile should be a light or dark tile or a highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)  # Draw a highlighted tile
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)  # Draw a regular tile

        # Add the chess piece icons, if any
        if self.occupying_piece is not None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)  # Blit the chess piece image onto the display at the square's position
