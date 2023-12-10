class student:
	class _Node:
		def __init__(self, name, reg, pro, cgpa):
			self.name = name
			self.regNo = reg
			self.program = pro
			self.cgpa = cgpa
			self.next = None

	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
		self.maxCGPA = 0

	def isEmpty(self):
		self.count == 0

	def addStudent(self, name, reg, pro, cgpa):
		newStd = self._Node(name, reg, pro, cgpa)
		if not self.isEmpty():
			newStd.next = self.head
			self.head = newStd
		else:
			self.head = self.tail = newStd
		if self.maxCGPA < cgpa:
			self.maxCGPA = cgpa
		self.count += 1

	def getMaxCGPA(self):
		return self.maxCGPA