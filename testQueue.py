from simpleQueue import *

def testEmptyQueue():
	q1 = simpleQueue()
	assert(q1.queueLength() == 0)
	assert(q1.queueEmpty())

def testEnqueue():
	q1 = simpleQueue()
	q1.queueAdd(10)
	q1.queueAdd(20)
	q1.queueAdd(30)
	assert(q1.queueLength() == 3)

def testDequeue():
	q1 = simpleQueue()
	q1.queueAdd(10)
	q1.queueAdd(20)

testEmptyQueue()
testEnqueue()