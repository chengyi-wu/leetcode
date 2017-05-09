class LRUCache(object):
	'''
	https://leetcode.com/problems/lru-cache/#/description
	Least Recently Used (LRU) cache
	'''
	def __init__(self, capacity):
		self.keyList = [] #index at 0 is most recently used object, tail is the least used one
		self.htable = { }
		self.capacity = capacity
		self.size = 0
		#print self.check()
		
	def get(self, key):
		if key not in self.htable:
			return -1
		#remove the element from the list and place it on the top of the list
		self.keyList.remove(key)	
		self.keyList.insert(0, key)
		print "get", key
		self.check()
		return self.htable[key]
		
	def put(self, key, value):
		if key in self.htable:
			self.keyList.remove(key)
		elif len(self.keyList) == self.capacity:
				k = self.keyList.pop()
				del self.htable[k]
				self.size -= 1
		
		self.keyList.insert(0, key)
		self.htable[key] = value
		self.size += 1
		print "put", key, value
		self.check()
		
	def check(self):
		print "KEYS", self.keyList
		print "HTABLE", self.htable
		print "SIZE", self.size
		
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