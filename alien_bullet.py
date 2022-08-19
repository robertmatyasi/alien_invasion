import pygame
from random import choice
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    """A class to manage bullets fired from aliens."""

    def __init__(self, ai_game):
        """Create a bullet object at the alien's's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width,
            self.settings.alien_bullet_height)
        shooter = choice(ai_game.aliens.sprites())
        self.rect.midtop = shooter.rect.midbottom
       
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += self.settings.alien_bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)