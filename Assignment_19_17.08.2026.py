#Create a class triangle with 3 variables side1, side2, side3. Initialize the variables with constructor. It also has the variables angle1, angle2, angle3. Create a class equilateral triangle and find the area of the triangle using calArea() function. Find the tangent of all angles using find angles method. Create a class scalene which is a child of triangle class. Find out the perimeter of the triangle using calPerimeter() function. Find out the area of the triangle using calArea() function. Use the math package for the computation. Print the area as a whole number.

import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        self.angle1 = 0
        self.angle2 = 0
        self.angle3 = 0


class Equilateral(Triangle):

    def __init__(self, side):
        super().__init__(side, side, side)

        self.angle1 = 60
        self.angle2 = 60
        self.angle3 = 60

    def calArea(self):
        area = (math.sqrt(3) / 4) * self.side1 * self.side1
        return area

    def findAngles(self):
        print("Tangent of angle 1 =", math.tan(math.radians(self.angle1)))
        print("Tangent of angle 2 =", math.tan(math.radians(self.angle2)))
        print("Tangent of angle 3 =", math.tan(math.radians(self.angle3)))


class Scalene(Triangle):

    def calPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def calArea(self):
        s = self.calPerimeter() / 2

        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        return area

    def findAngles(self):
        # Angle 1 opposite side1
        self.angle1 = math.degrees(
            math.acos(
                (self.side2**2 + self.side3**2 - self.side1**2)
                / (2 * self.side2 * self.side3)
            )
        )

        # Angle 2 opposite side2
        self.angle2 = math.degrees(
            math.acos(
                (self.side1**2 + self.side3**2 - self.side2**2)
                / (2 * self.side1 * self.side3)
            )
        )

        # Angle 3 opposite side3
        self.angle3 = 180 - self.angle1 - self.angle2

        print("Tangent of angle 1 =", math.tan(math.radians(self.angle1)))
        print("Tangent of angle 2 =", math.tan(math.radians(self.angle2)))
        print("Tangent of angle 3 =", math.tan(math.radians(self.angle3)))



side = float(input("Enter side of equilateral triangle: "))

e = Equilateral(side)

print("\nEquilateral Triangle")
print("Area =", round(e.calArea()))
e.findAngles()



side1 = float(input("\nEnter side 1 of scalene triangle: "))
side2 = float(input("Enter side 2 of scalene triangle: "))
side3 = float(input("Enter side 3 of scalene triangle: "))

s = Scalene(side1, side2, side3)

print("\nScalene Triangle")
print("Perimeter =", s.calPerimeter())
print("Area =", round(s.calArea()))
s.findAngles()