class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Health: {}\n".format(self.health)
		return self

class Dog(Animal):
	def __init__(self, name, health=150):
		super(Dog, self).__init__(name, health)
	def pet(self):
		self.health += 5
		return self


class Dragon(Animal):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name, health)
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		Animal.displayHealth(self)
		print "I am a dragon"
		# Do I need to return self here?
		return self

class Robin(Animal):
	def __init__(self, name, health):
		super(Robin, self).__init__(name, health)
	def sing(self):
		self.health += 1
		print "chirp chirp chrip"
		return self


fido = Dog("fido")
fido.displayHealth()
fido.walk()
fido.walk()
fido.walk()
fido.run()
fido.run()
fido.pet()
fido.displayHealth()
smaug = Dragon("Smaug")
smaug.displayHealth()
#fido.fly() #AttributeError
red = Robin("Red", 10)
#red.fly() #AttributeError
#red.pet() #AttributeError


