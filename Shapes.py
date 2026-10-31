class shape:
    def __init__(self, name):
        self.name=name
    def area(self):
            return 0
    def describe(self):
            print(f"{self.name} is a shape with an area of {self.area()}.")
class rectangle(shape):
    def __init__(self,name,height,width):
        super(). __init__(name)
        self.height=height
        self.width=width
    def width(self):
            return self.width
    def height(self):
            return self.height
    def area(self):
            return self.height*self.width
    def describe(self):
            print(f"{self.name} is a rectangle with an area of {self.area()}.")

class circle(shape):
    def __init__(self,name,radius):
        super(). __init__(name)
        self.radius=radius
    def radius(self):
            return self.radius
    def area(self):
            return 3.14*self.radius*self.radius
    def describe(self):
            print(f"{self.name} is a circle with an area of {self.area()}.")
a=shape("Generic Shape")
b=rectangle("Rectangle", 4, 5)
c=circle("Circle", 3)
a.describe()
b.describe()
c.describe()