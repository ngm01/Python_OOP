import time
class Call(object):
	def __init__(self, unique_id, name, number, call_time, reason):
		self.unique_id = unique_id
		self.name = name
		self.number = number
		try:
			time.strptime(call_time.replace(":", " "), "%I %M %p")
			self.call_time = call_time
		except ValueError:
			print "Time of call #{} formatted incorrectly. Times should be formatted like so: 8:05 PM.\nCall moved to end of queue automatically.".format(unique_id)
			self.call_time = "11:59 PM"
		self.reason = reason
		self.formatted_time = time.strptime(self.call_time.replace(":", " "), "%I %M %p")

	def displayCall(self):
		print "Unique ID: {}\nCaller Name: {}\nCaller Phone Number: {}\nTime of Call: {}\nReason for Call: {}\n".format(self.unique_id, self.name, self.number, self.call_time, self.reason)
		return self


class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def set_queue(self):
		self.queue_size = len(self.calls)

	def add(self, *args):
		#Hacker Level
		for i in args:
			if len(self.calls) >= 1:
				idx = 0
				for k in range(0, len(self.calls)):
					if i.formatted_time > self.calls[k].formatted_time:
						idx = k + 1
				self.calls.insert(idx, i)
			else:
				self.calls.append(i)
		self.set_queue()
		return self

	def remove(self):
		del self.calls[0]
		return self

	def info(self):
		self.set_queue()
		print "\nCalls in Queue: {}\n".format(self.queue_size)
		for i in self.calls:
			print "Call Details:\n--------------"
			i.displayCall()
		return self

	#Ninja Level
	def dropCall(self, call_to_drop):
		for i in self.calls:
			if call_to_drop == i.number:
				self.calls.remove(i)
		self.set_queue()
		return self





call1 = Call("12345", "Bob Smith", "555 555 5555", "8:07 PM", "test")
call2 = Call("87643", "Lauren Ipsum", "555 123 3421", "7:08 PM", "foobar")
call3 = Call('95673', "Larry Dairy", "555 345 9876", "10:05 AM", "moo")
call4 = Call("99999", "Val U. Error", "555 987 3214", "this is wrong", "can't give time in correct format")
call5 = Call('23456', "Baller Caller", '444 321 9876', "1:34 PM", "Wish I was taller")

verizon = CallCenter()

verizon.add(call1)
verizon.add(call2)
verizon.add(call3)
verizon.add(call4)
verizon.add(call5)

verizon.info()
verizon.dropCall('555 345 9876')
verizon.info()