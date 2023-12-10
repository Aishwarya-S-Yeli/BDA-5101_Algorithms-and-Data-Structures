from simpleStack import *

def testEmptyStack():
	s1 = simpleStack()
	assert (s1.elementCount() == 0)

def testpush():
	s1 = simpleStack()
	s1.stackPush(10)
	assert(s1.isEmpty() == False)
	assert(s1.elementCount() == 1)

def testpop():
	s1 = simpleStack()
	s1.stackPush(10)
	s1.stackPop()
	assert(s1.isEmpty())
	assert (s1.elementCount() == 0)

def testDisplay():
	s1 = simpleStack()
	s1.stackPush(10)
	s1.stackPush(20)
	s1.stackPush(30)
	s1.stackPush(40)
	s1.stackDisplay()

testEmptyStack()
testpush()
testpop()
testDisplay()