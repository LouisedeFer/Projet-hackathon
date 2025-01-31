
import pygame

# First party
from .dir import Dir

# Third party
import importlib.resources
import sys
from pathlib import Path





class Tile:
    """
    A square tile in the game.

    Includes a color.
    """

    def __init__(self, color: pygame.Color, number : str) -> None:
        """Object initialization."""
        self._color = color
        self._number=number
        self._font=None

    

    @property
    def number(self)-> int :
        """The number of the tile."""
        return self._number
    

    @property
    def color(self) -> pygame.Color:
        """The color of the tile."""
        return self._color

    @color.setter
    def color(self, color: pygame.Color) -> None:
        """Change the color of the tile."""
        self._color = color

    def __eq__(self, other: object) -> bool:
        """
        Check if two tiles are equal.

        Compare the x and y coordinates.
        """
        if isinstance(other, Tile):
            return self._x == other._x and self._y == other._y
        return False


    
    def draw(self, col, row, screen: pygame.Surface, size: int) -> None:
        """Draw the tile on screen."""
        if self._font is None : 
            with importlib.resources.path("project", "DejaVuSansMono-Bold.ttf") as f:
                self._font=pygame.font.Font(f, 32)
        rect = pygame.Rect(col * size, row* size, size, size)
        pygame.draw.rect(screen, self.color, rect)
        text = self._font.render(f"{self._number}", True, pygame.Color("red"))
        x, y = col*size + size/3, row*size + size/3 # Define the position where to write text.
        screen.blit(text, (x, y))
