class simpleStack:
	def __init__(self):
		self.data = []
		self.count = 0

	def isEmpty(self):
		return self.count == 0

	def elementCount(self):
		return self.count

	def stackPush(self, element):
		self.data.append(element)
		self.count += 1		

	def stackPop(self):
		if not self.isEmpty():
			self.count -= 1			
			return self.data.pop()		
		else:
			return None

	def stackPeek(self):
		if not self.isEmpty():
			return self.data[-1]
		else:
			return None

	def stackDisplay(self):
		if not self.isEmpty():
			for idx in range(len(self.data)):
				print (self.data[idx])
		else:
			return None

			