#Part I
class MathDojo(object):
	def __init__(self):
		self.sum = 0
	
	def add(self, *args):
		#was going to put a lot of edge case/evil test case checking in here, but time is at a premium, so...
		# if isinstance(arg, int) == False:
		# 	print "{} is not an int".format(arg)
		# elif args:
		for i in args:
		# 		if isinstance(i, int) == False:
		# 			print "{} is not an int".format(i)
				# else:
			self.sum += i
		return self

	def subtract(self, *args):
		for i in args:
			self.sum -= i
		return self

	def result(self, *args):
		print self.sum
		return self

md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result()

#Part II, with Part III modification to handle tuples

class MathDojoII(object):
	def __init__(self):
		self.sum = 0

	def add(self, *args):
		for i in args:
			if isinstance(i, list) or isinstance(i, tuple):
				for k in i:
					self.sum += k
			else:
				self.sum += i
		return self

	def subtract(self, *args):
		for i in args:
			if isinstance(i, list) or isinstance(i, tuple):
				for k in i:
					self.sum -= k
			else:
				self.sum -= i
		return self

	def result(self, *args):
		print self.sum
		return self

md2 = MathDojoII()

md2.add([1],3,4).add([3, 5], (7, 8), [2, 4.3, 1.25]).subtract(2, (2,3), [1.1, 2.3]).result()


