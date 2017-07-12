class MaxHeap(object):
	def __init__(self):
		self.heap = []
		self.keys = { } #Position in the heap
		self.values = { } #Frequency in the heap
	def swap(self, i, j):
		#print self.heap
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
		k1 = self.heap[i]
		k2 = self.heap[j]
		self.keys[k1] = i
		self.keys[k2] = j
	def maxheapify(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		largest = i
		if left < len(self.heap) and self.values[self.heap[left]] > self.values[self.heap[largest]]:
			largest = left
		if right < len(self.heap) and self.values[self.heap[right]] > self.values[self.heap[largest]]:
			largest = right	
			
		if i != largest:
			self.swap(i, largest)
			self.maxheapify(largest)
	def append(self, k):
		if k in self.heap:
			self.increaseKey(k)
		else:
			self.heap.append(k)
			self.keys[k] = len(self.heap) - 1
			self.values[k] = 1
	def increaseKey(self, k):
		self.values[k] += 1
		i = self.keys[k]
		p = (i - 1) / 2
		while p >= 0 and self.values[self.heap[i]] > self.values[self.heap[p]]:
			self.swap(p, i)
			i = p
			p = (i - 1) / 2
	def extractMax(self):
		print self.heap
		print self.keys
		print self.values
		self.swap(0, len(self.heap) - 1)
		k = self.heap.pop()
		
		del self.keys[k]
		del self.values[k]
		self.maxheapify(0)
		return k
	def __str__(self):
		return str(self.heap)
		

def topKFrequent(nums, k):
	heap = MaxHeap()
	results = []
	i = 0
	for n in nums:
		heap.append(n)
	while i != k:
		results.append(heap.extractMax())
		i += 1
	return results
	
print topKFrequent([2,2,3,1,1,1,1], 2)