class Slist:
	class _Node:
		def __init__(self, key):
			self.data = key
			self.next = None
			print ('Created: ',key)
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def getCount(self):
		return self.count		

	def isEmpty(self):
		return self.count == 0

	def addAtHead(self, ele):
		new_node = self._Node(ele)

		if not self.isEmpty():
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = self.tail = new_node
		self.count += 1

	def addAtTail(self, ele):
		new_node = self._Node(ele)

		if not self.isEmpty():
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = self.tail = new_node
		self.count += 1

	def isMember(self, key):
		if not self.isEmpty():
			current = self.head
			while current != None:
				if current.data == key:
					break
				else:
					current = current.next
			return current != None
		else:
			return False

	def deleteAtHead(self):
		if not self.isEmpty():
			data = self.head.data
			self.head = self.head.next
			if self.head == None:
				self.tail = None
			self.count -= 1
			return data
		else:
			return None

	def deleteAtTail(self):
		if not self.isEmpty():
			data = self.tail.data
			if self.count == 1:
				self.head = self.tail = None
			else:
				last = self.tail
				current = self.head
				while current.next != last:
					current = current.next
				current.next = None
				self.tail = current
			self.count -= 1
			return data
		else:
			return None

s1 = Slist()
s1.addAtHead(10)

