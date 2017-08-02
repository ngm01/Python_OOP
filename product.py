class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status

	def changeStatus(self):
		if self.status == "for sale":
			self.status = "sold"
		else:
			self.status = "for sale"
		return self

	def addTax(self, decimal):
		if isinstance(decimal, float) == False or decimal >= 1:
			print "Sales tax must be in decimal format (e.g. .06). You entered {}".format(decimal)
		else:
			self.price += self.price * decimal
		return self.price

	def whyReturn(self, reason):
		if isinstance(reason, str) == False:
			print "{} is not a valid reason for a return.".format(reason)
		else:
			if reason == "defective":
				self.status = "defective"
				self.price = 0.0
			elif reason == "in box":
				self.status = "for sale"
			elif reason == "box opened":
				self.status = "used"
				self.price += self.price * .2
			else:
				print "Thanks for the return"
			return self

	def displayInfo(self):
		print "Price: ${}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: ${}\nStatus: {}\n".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)
		return self

widget = Product(50, "Widget 9000", "1oz", "Stuff Inc", 100)
widget.displayInfo()
widget.addTax(.06)
print widget.price
widget.whyReturn("box opened")
print widget.price
print widget.status
widget.whyReturn(123)
widget.addTax(1)