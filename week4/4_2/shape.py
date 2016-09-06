#!/usr/local/bin/python3
# NAME: NESTOR ALVAREZ
# FILE: shape.py
# DESC: A Shape class from The Quick Python Book (p. 30), set x,y coordinates,
#       moves objects, and reports location.

import math

class Shape:
    
    def __init__(self, x, y):
        """Assign x,y coordinates to the object"""
        self.x = x
        self.y = y


    def move(self, deltaX, deltaY):
        """Moves Shape object by adding values to the object's x and y coordinates."""
        self.x = self.x + deltaX
        self.y = self.y + deltaY

    def location(self):
        return (self.x, self.y)
    
    def __str__(self):
        """Return class name, x, and y"""
        return "{}, x:{}, y:{}".format(type(self).__name__, self.x, self.y)

def __main__():
    """Testing Shape class move(), location(), and __str__() methods"""
    print("--- START ---")
    i2 = 0 
    c1 = Shape(0, 5)
    c2 = Shape(5, 5)
    for i in range(10):
        i2 += i 
        c1.move(i, i)
        c2.move(i, i2) 
        print('--')
        print('Shape 1: ',c1)
        print('Shape 2: ',c2)
    print(c1.location())
    print(c2.location())

    print("--- END ---")


if __name__ == '__main__':
      __main__()
