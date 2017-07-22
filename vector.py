from math import sin, cos, pi, sqrt

class Vector():
    
    def __init__(self, x, y):
        '''Create 2D vector'''
        self.basex = self.x = x
        self.basey = self.y = y
        self.rotation = 0

    def rotate(self, angle):
        '''Rotate around the center, angle in degrees'''
        self.rotation += angle
        rad = self.rotation * 2 * pi / 360
        self.x = - self.basex * cos(rad) + self.basey * sin(rad)
        self.y = self.basex * sin(rad) + self.basey * cos(rad)

    def lenght(self):
        '''Lenght of the vector'''
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __add__(self, other):
        '''Sum of 2 vectors'''
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __iadd__(self, other):
        '''Increases 1 vector by the value of another one'''
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        '''Substraction of vectors'''
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __isub__(self, other):
        '''Decreese 1 vector by the value of another one'''
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, number):
        '''Multiplication of vector lenght by number'''
        x = self.x * number
        y = self.y * number
        return Vector(x, y)
    def __imul__(self, number):
        '''Increase of vector number times'''
        self.x = self.x * number
        self.y = self.y * number
        return self

    def __truediv__(self, number):
        '''Division of vector lenght by number'''
        x = self.x / number
        y = self.y / number
        return Vector(x, y)
    def __itruediv__(self, number):
        '''Division of vector lenght by number'''
        self.x = self.x / number
        self.y = self.y / number
        return self