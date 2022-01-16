#%%
import math
class Circle:
    def __init__(self,radius=1.0,color="red"):
        self.setRadius(radius)
        self.__color = color
    
    def setRadius(self,radius):
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 1.0
    
    def setColor(self,color):
        self.__color = color
        
    def getColor(self):
        return self.__color

    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return math.pi * math.pow(self.__radius,2)
    
    def __str__(self):
        return "Circle: Radius {:.2f} Color {}".format(self.getRadius(),self.getColor())
    

class Cylinder(Circle):
    def __init__(self,radius=1.0,color="red",height=1.0):
        super().__init__(radius,color)
        self.setHeight(height)
        
    def setHeight(self,height):
        if height > 0:
            self.__height = height
        else:
            self.__height = 1.0
    
    def getHeight(self):
        return self.__height
    
    def getVolume(self):
        return super().getArea() * self.getHeight()

    def __str__(self):
        return super().__str__() + " Cylinder: Height {:.2f}".format(self.getHeight())


#%%
