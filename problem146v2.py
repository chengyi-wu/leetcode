import collections
class LRUCache(object):
	'''
	https://leetcode.com/problems/lru-cache/#/description
	Least Recently Used (LRU) cache
	implementation using OrderedDict
	'''
	def __init__(self, capacity):
		self.cache = collections.OrderedDict()
		self.capacity = capacity
		self.size = 0
		#print self.check()
		
	def get(self, key):
		if key not in self.cache:
			return -1
		#remove the element from the list and place it on the top of the list
		v = self.cache[key]
		del self.cache[key]
		self.cache[key] = v
		print "get", key
		self.check()
		return v
		
	def put(self, key, value):
		if key in self.cache:
			del self.cache[key]
			self.size -= 1
		elif self.size == self.capacity:
				self.cache.popitem(last=False)
				self.size -= 1
		
		self.cache[key] = value
		self.size += 1
		print "put", key, value
		self.check()
		
	def check(self):
		print "ORDEREDDICT", self.cache
		print "SIZE", self.size
		print ">>>>>>>"
		
def test_LRUCache():
	cache = LRUCache(2)
	
	cache.put(1, "ITEM#1")
	cache.put(2, "ITEM#2")
	cache.put(2, "ITEM#2")
	cache.put(3, "ITEM#3")
	print cache.get(1)
	print cache.get(2)

import cProfile	
cProfile.run('test_LRUCache()')