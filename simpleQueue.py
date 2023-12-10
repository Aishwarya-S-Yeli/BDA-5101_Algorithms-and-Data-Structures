class simpleQueue:
	def __init__(self):
		self.data = []
		self.count = 0

	def queueLength(self):
		return self.count

	def queueEmpty(self):
		return self.count == 0

	def queueFirst(self):
		if not self.queueEmpty():
			return self.data[0]

	def queueAdd(self, ele):
		self.data.append(ele)
		self.count += 1

	def queueDelete(self):
		if not self.queueEmpty():
			self.count -= 1
			return self.data.pop(0)
		else:
			return None

