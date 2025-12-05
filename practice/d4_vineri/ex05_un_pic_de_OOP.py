# un pic de OOP

import math

class Point:
    # atribute: x și y

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return str(self.as_tuple())
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        dist = math.sqrt(
            self.x ** 2 + self.y ** 2
        )
        return dist
    
    def as_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()
    
    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()
    

class ThreeDPoint(Point):
    pass