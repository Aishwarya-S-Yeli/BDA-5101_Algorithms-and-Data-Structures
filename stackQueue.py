from flexiQ import *

class specialStack:
	def __init__(self):
		self.q1 = flexiQueue()

	def stackPush(self, val):
		self.q1.enqueue(val)

	def stackPop(self):
		count = self.q1.length()
		if count != 0:
			while(count != 1):
				self.q1.enqueue(self.q1.dequeue())
				count -= 1
			data = self.q1.dequeue()
			return data
		else:
			return None


def test_stack():
	s1 = specialStack()
	s1.stackPush(10)
	s1.stackPush(20)
	s1.stackPush(30)
	s1.stackPush(40)
	assert(s1.stackPop() == 40)
	s1.stackPush(50)
	assert(s1.stackPop() == 50)


test_stack()