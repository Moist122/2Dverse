import pygame
from pygame.sprite import Sprite

class Mine(Sprite):

    def __init__(self, screen, position):
        '''Create mine in given place'''
        super().__init__()
        self.screen = screen
        self.position = position

        # Load image and get its rect
        self.image = pygame.image.load('images/mine.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

        # Mine stats
        self.speed = 1
        self.range = 500
        self.beep_cd = 50

    def draw(self):
        '''Draw a mine to the screen'''
        self.screen.blit(self.image, self.rect)

    def move(self, ship):
        '''Move in direction of the ship.'''
        path = ship.position - self.position
        if path.lenght() < self.range:
            movement = path / path.lenght() * self.speed
            self.position += movement
            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y