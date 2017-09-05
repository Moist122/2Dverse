import pygame
from os.path import join

from vector import Vector
from bullet import Bullet

class Ship():

    def __init__(self, screen):
        """Initialize ship with basic statistics."""
        self.screen = screen
        
        # Load image, get surface and rect
        self.image = pygame.image.load(join('images', 'ship.png'))
        self.surface = self.basesurface = pygame.Surface((40, 62))
        self.basesurface.blit(self.image, (0, 0))
        self.rect = self.basesurface.get_rect()
        self.screen_rect = screen.get_rect()

        # Set starting position
        x = self.screen_rect.centerx
        y = self.screen_rect.bottom - self.rect.height
        self.position = Vector(x, y)
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)
        
        # Set direction, speed and angle of rotation (degrees)
        self.direction = Vector(0, -1)
        self.acceleration = 1
        self.speed = Vector(0, 0)
        self.rotation = 0

        # Movement and firing flags
        self.accelerating = False
        self.slowing_down = False
        self.rotating_right = False
        self.rotating_left = False
        self.shooting = False
        
        # Gameplay constants
        self.max_hp = 100
        self.shot_cd = 20
        self.invulnerable_time = 30
        self.speed_limit = 10 # Not implemented
        self.bullet_speed = 3
        self.movement_cd = 30

        # Gameplay variables
        self.hp = 100
        self.shot_actual_cd = 0
        self.invulnerable_actual_time = 0
        self.acceleration_actual_cd = 0
        self.turning_actual_cd = 0

    def draw(self):
        ''' Draw ship on screen.'''
        self.screen.blit(self.surface, self.rect)

    def accelerate(self):
        '''Increase speed by the acceleration in direction of the ship.'''
        self.speed += self.direction * self.acceleration

    def slow_down(self):
        '''
        Decrease ship's speed by half in both directions.
        If it is too slow stop it.
        '''
        if abs(self.speed.x)<=1:
            self.speed.x = 0
        else:
            self.speed.x = self.speed.x / 2
        
        if abs(self.speed.y)<=1:
            self.speed.y = 0
        else:
            self.speed.y = self.speed.y / 2

    def update(self):
        '''Update according to flags and cooldowns'''
        if not self.acceleration_actual_cd:
            if self.accelerating:
                self.accelerate()
                self.acceleration_actual_cd = self.movement_cd
            elif self.slowing_down:
                self.slow_down()
                self.acceleration_actual_cd = self.movement_cd
        
        if not self.turning_actual_cd:
            if self.rotating_left:
                self.rotate(90)
                self.turning_actual_cd = self.movement_cd
            if self.rotating_right:
                self.rotate(-90)
                self.turning_actual_cd = self.movement_cd

    def move(self):
        '''Move the ship by the amount of speed.'''
        self.position += self.speed
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)

    def rotate(self, angle):
        '''Rotate the ship around it's center by angle in degrees.'''
        self.rotation += angle
        self.direction.rotate(angle)
        self.surface = pygame.transform.rotate(self.basesurface, self.rotation)
        self.rect = self.surface.get_rect()
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def cooldowns(self):
        '''Decrease all cooldowns by 1.'''
        if self.acceleration_actual_cd:
            self.acceleration_actual_cd -= 1
        if self.turning_actual_cd:
            self.turning_actual_cd -= 1
        if self.shot_actual_cd:
            self.shot_actual_cd -= 1
        if self.invulnerable_actual_time:
            self.invulnerable_actual_time -= 1
    
    def shoot(self, bullets):
        '''Shoot a bullet if possible.'''
        if self.shooting and not self.shot_actual_cd:
            bullet = Bullet(self.screen, self)
            bullets.add(bullet)
            self.shot_actual_cd = self.shot_cd