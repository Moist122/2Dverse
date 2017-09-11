import pygame
from os.path import isfile, join
from mine import Mine
from vector import Vector

class Map():
    '''Actual map.'''

    def __init__(self, ship, screen, bullets, enemies):
        self.ship = ship
        self.screen = screen
        self.bullets = bullets
        self.enemies = enemies

    def load_map(self, name):
        '''Load a new map.'''
        if isfile(join('maps', 'session', name+'.txt')):
            directory = join('maps', 'session', name+'.txt')
        elif isfile(join('maps', name+'.txt')):
            directory = join('maps', name+'.txt')
        else:
            return "Map error"
        # save left map
        self.name = name
        self.open(directory)

    def open(self, directory):
        '''Opens new map'''
        self.bullets.empty()
        self.enemies.empty()
        #self.ship.position = self.position
        with open(directory) as location:
            for line in location.readlines():
                data = line.split()
                if data[0] == 'mine':
                    self.enemies.add(Mine(self.screen,
                        Vector(int(data[1]), int(data[2])), self.ship))