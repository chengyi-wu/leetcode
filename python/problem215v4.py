import heapq	
def findKthLargest(nums, k):
	#buid maxheap
	heapq.heapify(nums)
	return heapq.nlargest(k, nums)[-1]

	pq = []
	k = len(nums) - k
	i = 0
	while len(pq) < k:
		heapq.heappush(pq,nums[i])
		i += 1
	print pq
	return max(pq)
	
print findKthLargest([3,2,1,5,6,4], 2)
print findKthLargest([1,4,4],2)