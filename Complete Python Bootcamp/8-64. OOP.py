import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = math.sqrt(((self.coor1[0] - self.coor2[0])**2 +
                              (self.coor1[1] - self.coor2[1])**2))
        return distance

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


line = Line((3, 2), (8, 10))
print(line.distance())
print(line.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius**2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.height


cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
