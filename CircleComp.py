import math


class CircleComp:
    radius = float(input("Enter radius for the circle: "))
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius


print(f"Diameter of the Circle: {CircleComp.diameter}")
print(f"Circumference of the Circle: {CircleComp.circumference}")
print(f"Area of the Circle: {CircleComp.area}")
