class MaxHeap(object):
	def __init__(self):
		self.heap = []
	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	def append(self, k):
		self.heap.append(k)
		n = len(self.heap) - 1
		parent = (n - 1) / 2
		while parent >= 0 and self.heap[n] > self.heap[parent]:
			self.swap(n, parent)
			n = parent
			parent = (n - 1) / 2
	def getMax(self):
		return self.heap[0]
	def maxheapify(self, i):
		left = 2 * i + 1
		right = 2 * i + 2
		largest = i
		if left < len(self.heap) and self.heap[largest] < self.heap[left]:
			largest = left
		if right < len(self.heap) and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != i:
			self.swap(i, largest)
			self.maxheapify(largest)
	def extractMax(self):
		self.swap(0, len(self.heap) - 1)
		m = self.heap.pop()
		self.maxheapify(0)
		return m
	def __str__(self):
		return str(self.heap)
		
		
def findKthLargest(nums, k):
	#buid maxheap
	heap = MaxHeap()
	for n in nums:
		heap.append(n)
	#print heap
	i = 0
	m = heap.getMax()
	while i != k:
		m = heap.extractMax()
		print m, heap
		i += 1
	return m
	
print findKthLargest([3,2,1,5,6,4], 2)