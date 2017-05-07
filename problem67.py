def addBinary(a, b):
	p1 = len(a) - 1
	p2 = len(b) - 1
	carryover = 0
	result = ""
	while p1 >= 0 or p2 >= 0: 
		d = carryover
		if p1 >= 0:
			d += int(a[p1])
			p1 -= 1
		if p2 >= 0:
			d += int(b[p2])
			p2 -= 1
		carryover = d / 2	
		d  %= 2
		result = str(d) + result
		
	if carryover != 0:
		result = str(carryover) + result
	return result
	
def test_addBinary():
	print addBinary("110", "10")
	print addBinary("11", "11")
	print addBinary("1", "10")
	
test_addBinary()
		