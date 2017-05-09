class Interval(object):
	def __init__ (self, s = 0, e = 0):
		self.start = s
		self.end = e
	def __str__(self):
		return "[" + str(self.start) + ", " + str(self.end) + "]"

def merge(intervals):
	print intervals
	if len(intervals) == 0:
		return intervals
	def getStart(interval):
		return interval.start
	intervals.sort(key = getStart)
	results = [intervals[0]]
	for i in range(1, len(intervals)):
		last = results[-1]
		if intervals[i].start  <= last.end:
			results.pop()
			left = min(last.start, intervals[i].start)
			right = max(last.end, intervals[i].end)
			results.append([left, right])
		else:
			#results.append(last)
			results.append(intervals[i])
		#print results[-1]
	print results
	return results
	
def test():
	intervals = []
	intervals.append(Interval(2,3))
	intervals.append(Interval(4,5))
	intervals.append(Interval(1,10))
	#intervals.append(Interval(2,3))
	
	def getStart(interval):
		return interval.start
	
	intervals.sort(key=getStart)
	for i in intervals:
		print i
	
test()