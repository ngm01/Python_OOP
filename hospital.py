class Hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = [] * self.capacity
		self.beds = ["Empty"] * self.capacity

	def admit(self, *args):
		for p in args:
			if "Empty" not in self.beds:
				print "Sorry, {}. The hospital is full.".format(p.name)
			else:
				for b in self.beds:
					if b == "Empty":
						p.bed_number = self.beds.index(b) + 1
						self.beds[self.beds.index(b)] = p.id_num
						print "Patient {} (id #{}) admitted to bed #{}".format(p.name, p.id_num, p.bed_number)
						self.patients.append(p)
						break


	def discharge(self, *args):
		for i in args:
			for p in self.patients:
				if i == p.id_num:
					self.patients.remove(p)
					self.beds[self.beds.index(i)] = "Empty"
		

class Patient(object):
	def __init__(self, id_num, name, *allergies):
		self.id_num = id_num
		self.name = name
		self.allergies = allergies
		self.bed_number = None

norton = Hospital("Norton", 2)
print norton.beds
p1 = Patient("1234", "Bob Smith", "shellfish")
p2 = Patient("3456", "Lauren Ipsum", "peanuts", "gluten")
p3 = Patient("8765", "Larry Dairy", "lactose")

norton.admit(p1, p2, p3)
#print norton.patients
print norton.beds
norton.discharge('3456')
#print norton.patients
print norton.beds