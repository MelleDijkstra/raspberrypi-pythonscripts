class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point created")

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)

    def __sub__(self,other):
        return Vector(self.x - other.x,self.y + other.y)

    def __str__(self):
        return "x: "+str(self.x)+" y: "+str(self.y)

class Vector:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Vector created")

    def __str__(self):
        return "x: "+str(self.x)+" y: "+str(self.y)

p = Point(-4,-3)
i = Point(-1,-1)

v = p - i

print("p location: ("+str(p.x)+", "+str(p.y)+")")
print("i location: ("+str(i.x)+", "+str(i.y)+")")
print("Distance from each other ("+str(v)+")")

isRunning = True
