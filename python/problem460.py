class KeyValuePair(object):
		def __init__(self, k, v):
			self.key = k
			self.val = v
		def __str__(self):
			return "(" + str(self.key) + "," + str(self.val) + ")"

class PriorityQueue(object):		
	def __init__(self, capacity):
		self.size = 0
		self.capacity = capacity
		self.bucket = []
		self.keyIndex = { }
		self.hashtable = { }
	def getParent(self, n):
		i = (n - 1) / 2
		return i
	def getLeft(self, n):
		i = 2 * n + 1
		return i
	def getRight(self, n):
		i = 2 * n + 2
		return i
	def insert(self, key, value):
		if self.size == self.capacity:
			raise
		self.bucket.append(KeyValuePair(key, 1))
		self.keyIndex[key] = self.size
		self.hashtable[key] = value
		#for i in range(self.size, self.size / 2 - 1, -1):
		self.size += 1
		self.minify()
		
		return
	def extractMin(self):
		if self.size == 0:
			raise
		key = self.bucket[0].key
		val = self.hashtable[key]
		self.bucket.pop(0)
		del self.keyIndex[key]
		del self.hashtable[key]
		self.size -= 1
		#print "EXTRACT MINI", self.size
		self.minify()
		#self.check()
		return val
	def getMin(self):
		if self.size == 0:
			raise
		return self.hashtable[self.bucket[0].key]
	def swap(self, i, j):
		temp = self.bucket[i]
		self.bucket[i] = self.bucket[j]
		self.bucket[j] = temp
		
		self.keyIndex[self.bucket[i].key] = i
		self.keyIndex[self.bucket[j].key] = j
		
	def minify(self):
		print "MINIFY"
		for i in range(self.size - 1, self.size / 2 - 1, -1):
			parent = self.getParent(i)
			if self.bucket[parent].val > self.bucket[i].val:
				self.swap(parent, i)
			#n = parent
		self.check()
	def increaseKey(self, key):
		i = self.keyIndex[key]
		self.bucket[i].val += 1
		#for i in range(self.size - 1, self.size / 2 - 1, -1):
		self.minify()
		self.check()
	def check(self):
		print "BUCKET:", 
		for i, key in enumerate(self.bucket):
			print str(key),
		print ""
		print self.hashtable
		print self.keyIndex
	def put(self, key, value):
		if self.size == self.capacity and key not in self.keyIndex:
			self.extractMin()
			
		if key in self.keyIndex:
			self.increaseKey(key)
			self.hashtable[key] = value
		else:
			self.insert(key, value)
		
	def get(self, key):
		if key not in self.keyIndex:
			return -1
		self.increaseKey(key)
		self.check()
		return self.hashtable[key]
		

class LFUCache(object):
	'''
	https://leetcode.com/problems/lfu-cache/#/description
	Least Frequently Used (LRU) cache 
	https://en.wikipedia.org/wiki/Least_frequently_used#Problems
	This is priority queue
	'''
	def __init__(self, capacity):
		self.keyCount = { }
		self.htable = { }
		self.capacity = capacity
		self.size = 0
		
	def get(self, key):
		if key not in self.keyCount:
			return -1
		self.keyCount[key] += 1
		print "get", key
		self.check()
		return self.htable[key]
		
	def put(self, key, value):
		if key not in self.keyCount:
			if self.size < self.capacity:
				self.size += 1
			else:
				#get the min value from keyCount and remove it
				k = min(zip(self.keyCount.values(), self.keyCount.keys()))[1]
				print "EVICT", k
				del self.keyCount[k]
				del self.htable[k]
			self.keyCount[key] = 0
			
		
		self.keyCount[key] += 1
		self.htable[key] = value
		print "put", key, value
		self.check()
		
	def check(self):
		print "\tKEYS", self.keyCount
		print "\tHTABLE", self.htable
		print "\tSIZE", self.size
		
def test_LFUCache():
	cache = PriorityQueue(2)
	
	cache.put(1, "ITEM#1")
	cache.put(2, "ITEM#2")
	cache.put(2, "ITEM#2")
	cache.put(3, "ITEM#3")
	print cache.get(1)
	print cache.get(2)
	
def test_PriorityQueue():
	q = PriorityQueue(5)
	q.insert(4, "TTTT")
	q.insert(2, "TT")
	q.insert(1, "ONE")
	q.increaseKey(4)
	print "MIN:" , q.getMin()
	print q.extractMin()

#test_PriorityQueue()
test_LFUCache()
#import cProfile	
#cProfile.run('test_LFUCache()')