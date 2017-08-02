class Bike(object):
	def __init__(self, price, max_speed, miles = 0):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "Price: ${}".format(self.price)
		print "Max Speed: {}".format(self.max_speed)
		print "Total Miles: {}".format(self.miles)
		return self

	def ride(self):
		print "Riding..."
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing..."
		self.miles -= 5

	def testDrive(self, rides, reverses):
		print "------------------"
		for i in range(1, rides + 1):
			self.ride()
		for k in range(1, reverses + 1):
			self.reverse()
		self.displayInfo()
		print ""

bike1 = Bike(200, "25mph")
bike2 = Bike(15, "60mph")
bike3 = Bike(.25, "30,000mph")



print "Bike 1:"
bike1.testDrive(3, 1)
print "Bike 2:"
bike2.testDrive(2, 2)
print "Bike 3:"
bike3.testDrive(0, 3)

