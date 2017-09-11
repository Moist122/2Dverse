import pygame
from enemy import Enemy
from pygame.sprite import Sprite
from os.path import join

class Mine(Enemy):

    def __init__(self, screen, position, ship):
        '''Create mine in given place'''
        super().__init__()
        self.screen = screen
        self.position = position
        self.ship = ship

        # Load image and get its rect
        self.image_on = pygame.image.load(join('images', 'mine_on.png'))
        self.image_off = pygame.image.load(join('images', 'mine_off.png'))
        self.rect = self.image_on.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

        # Mine stats
        self.speed = 1.5
        self.range = 300
        self.beep_cd = 50
        self.beep_actual_cd = 50
        self.active = False
        self.beep_on = True

    def draw(self):
        '''Draw a mine to the screen'''
        if self.beep_on:
            self.screen.blit(self.image_on, self.rect)
        else:
            self.screen.blit(self.image_off, self.rect)

    def move(self):
        '''Move in direction of the ship.'''
        path = self.ship.position - self.position
        if path.lenght() < self.range:
            self.active += 1
        if self.active:
            movement = path / path.lenght() * self.speed
            self.position += movement
            self.rect.centerx = self.position.x
            self.rect.centery = self.position.y

    def cooldowns(self):
        '''Beeps before exploding.'''
        if self.active:
            self.beep_actual_cd -= 1
            if self.beep_actual_cd == 0:
                self.beep_cd -= 10
                self.beep_actual_cd = self.beep_cd
                if self.beep_cd <= 0:
                    # placeholder start
                    print("boom")
                    self.active = False
                    self.range = 0
                    # placeholder end
                    #self.boom()
                elif self.beep_on:
                    self.beep_on -= 1
                else:
                    self.beep_on += 1
    
    def update(self):
        '''Move and update cooldowns.'''
        self.move()
        self.cooldowns()
