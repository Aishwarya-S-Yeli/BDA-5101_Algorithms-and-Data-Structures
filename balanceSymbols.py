from simpleStack import *

def balanceSymbols(data, stk):
	lefty = '{([';
	righty = '})]'

	for ch in data:		
		if ch in lefty:			
			stk.stackPush(ch)			
		elif ch in righty:
			if stk.isEmpty():
				return False			
			if righty.index(ch) != lefty.index(stk.stackPop()):	
				return False

	
	return (stk.isEmpty())

def testBalanceSymbols(data):
	stk = simpleStack()
	return balanceSymbols(data, stk)

assert(testBalanceSymbols('main(){ if ( x[10] == 20 ) { print(x)} }')==True)
