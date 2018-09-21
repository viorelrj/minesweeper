class Positionable:
	# initializer method
	def __init__(self, x, y):
		self.x = x
		self.y = y

		#print out to the console The mine coordinates
	def printCoordinates(self):
		print("x:{} y:{}".format(self.x, self.y))

class Mine (Positionable):
	self.type = "mine"


class Indicator (Positionable):
	self.type = "indicator"


class flag (Positionable):
	self.type = "flag"
