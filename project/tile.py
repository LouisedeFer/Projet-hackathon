
import pygame

# First party
from .dir import Dir

# Third party
import importlib.resources
import sys
from pathlib import Path


#Download font
with importlib.resources.path("project", "DejaVuSansMono-Bold.ttf") as f:
    font=pygame.font.Font(f, 32)


class Tile:
    """
    A square tile in the game.

    Includes a color.
    """

    def __init__(self, x: int, y: int, color: pygame.Color, number : int) -> None:
        """Object initialization."""
        self._x = x # Column index
        self._y = y # Line index
        self._color = color
        self._number=number

    @property
    def number(self)-> int :
        """The number of the tile."""
        return self._number
    

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the tile."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """Set the x coordinate."""
        self._x = value

    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the tile."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """Set the y coordinate."""
        self._y = value

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


    
    def draw(self, screen: pygame.Surface, size: int) -> None:
        """Draw the tile on screen."""
        rect = pygame.Rect(self.x * size, self.y * size, size, size)
        pygame.draw.rect(screen, self.color, rect)
        text = font.render("GAME OVER", True, pygame.Color("red"))
        x, y = self.x*size + size/2, self.y*size + size/2 # Define the position where to write text.
        screen.blit(text, (x, y))

        
