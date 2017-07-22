import pygame
from pygame.sprite import Sprite
from copy import copy

class Bullet(Sprite):

    def __init__(self, screen, ship):
        '''Create bullet'''
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create surface and get its rect
        self.surface = self.basesurface = pygame.Surface((4, 20))
        self.rect = self.basesurface.get_rect()

        # Set speed, position and rotation of the bullet
        self.speed = ship.direction * ship.bullet_speed + ship.speed
        self.position = copy(ship.position)
        self.rotation = 0
        self.rotate(ship.rotation)

    def rotate(self, angle):
        '''Rotate bullet around its center'''
        self. rotation += angle
        self.surface = pygame.transform.rotate(self.basesurface, self.rotation)
        self.rect = self.surface.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    
    def update(self):
        '''Update position of the bullet.'''
        self.position += self.speed
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, (230, 60, 20), self.rect)
        

