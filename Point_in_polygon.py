class Wall(object):
	def __init__(self, polyCorners, polyX, polyY):
		self.polyCorners = polyCorners 
		self.polyX = polyX             
		self.polyY = polyY             
		self.constant = []
		self.multiple = []

	def precalc_values(self):
		j = self.polyCorners - 1
		for i in range(0, self.polyCorners):
			if self.polyY[j] == self.polyY[i]:
				self.constant.append(self.polyX[i])
				self.multiple.append(0)
			else:
				self.constant.append(self.polyX[i]-(self.polyY[i]*self.polyX[j])/(self.polyY[j]-self.polyY[i])+(self.polyY[i]*self.polyX[i])/(self.polyY[j]-self.polyY[i]))
				self.multiple.append((self.polyX[j]-self.polyX[i])/(self.polyY[j]-self.polyY[i]))
				j = i

	def pointInPolygon(self, x, y): 
		oddNodes = False
		current = self.polyY[self.polyCorners-1] > y
		for i in range(0, self.polyCorners):
			previous = current
			current = self.polyY[i] > y
			if current != previous:
				oddNodes ^= y * self.multiple[i] + self.constant[i] < x
		return oddNodes 
