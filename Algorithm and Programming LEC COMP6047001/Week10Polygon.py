import math

class Polygon: 
	def __init__(self, no_of_sides): 
		self.n = no_of_sides 
		self.sides = [0 for i in range(no_of_sides)] 

	def inputSides(self): 
		self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)] 

	def dispSides(self): 
		for i in range(self.n): 
			print("Side",i+1,"is",self.sides[i]) 

# class Triangle(Polygon): 
	def __init__(self): 
		Polygon.__init__(self,3) 
	def findArea(self): 
		a, b, c = self.sides 
		# calculate the semi-perimeter 
		s = (a + b + c) / 2 
		area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
		print('The area of the triangle is %0.2f'%area)

class Hexagon(Polygon): 
	def __init__(self): 
		Polygon.__init__(self,6) 
	def findArea(self): 
		a, b, c, d, e, f = self.sides 
		# calculate the semi-perimeter 
		s = (a + b + c + d + e + f) / 2 
		area = 3 * math.sqrt(3) * s ** 2 / 2
		print(f'The area of the triangle is {area}')

# p = Polygon(6)
# p.inputSides()
# p.dispSides()

h = Hexagon()
h.inputSides()
h.dispSides()
h.findArea()