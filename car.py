class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12

		self.display_all()

	def display_all(self):
		print "Price: ${}\nSpeed: {}\nFuel: {}\nMileage: {}\nTax: {}\n".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

def makeCars(num):
	import random
	prices = [2000, 5000, 12000, 20000]
	speeds = ['100mph', '80mph', '25mph', '200mph']
	fuels = ["Full", "Kind of Full", "Not Full", "Empty"]
	mileages = ["15mpg", "20mpg", "25mpg", "30mpg"]
	cars = ["car" + str(i) for i in range(num)]
	for k in range(num):
		cars[k] = Car(prices[random.randint(0, 3)], speeds[random.randint(0, 3)], fuels[random.randint(0, 3)], mileages[random.randint(0, 3)])


makeCars(6)