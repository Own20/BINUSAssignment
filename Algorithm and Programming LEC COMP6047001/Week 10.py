# class Object:
#     pass
# class X(Object):
#     pass
# class Y(Object):
#     pass
# class Z(Object):
#     pass
# class A(X, Y):
#     pass
# class B(Y, Z):
#     pass
# class M(A, B, Z):
#     pass

# print("\033[0;31;40m Bright Red")
# print("\033[0;32;40m Bright Green")
# print("\033[0;33;40m Yellow")
# print("\033[0;34;40m Bright Blue")
# print("\033[0;35;40m Bright Magenta")
# print("\033[0;36;40m Bright Cyan")
# print("\033[0;37;40m White")

class Circle:
    def __init__(self, radius):
        self.radius = radius 

	def inputRadius(self): 
		self.radius = float(input("Enter radius: ")) 

	def dispRadius(self): 
		print("Radius is " + self.radius)

class Cylinder:
    def __init__(self): 
		Circle.__init__(self, 1)

    def inputHeight(self): 
		self.height = float(input("Enter height: "))

    def getHeight(self):
        return self.height
    
    def findVolume(self):
        s = self.sides
        h = self.height
        area = 3.14 * s * s * h
        print(f"The area is {area}")