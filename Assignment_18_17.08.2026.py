#Create a class shape with variable radius.
#Initialize the variable with constructor.
#Define a method calArea() to calculate sum of area of circle using math package. 
#Create a class sphere which is a child of the shape class.
#Define calVolume() to calculate volume of the sphere.

import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        area = math.pi * self.radius * self.radius
        return area


class Sphere(Shape):
    def calVolume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        return volume

radius = float(input("Enter radius: "))

s = Sphere(radius)

print("Area of circle =", s.calArea())

print("Volume of sphere =", s.calVolume())