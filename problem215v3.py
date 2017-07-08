import random
def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
    return
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def partition(nums, p, r):
    i = random.randint(p, r)
    swap(nums, i, r)
    x = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] >= x:
            i += 1
            swap(nums, i, j)
    i += 1
    swap(nums, i, r)
    return i

def select(nums, p, r, i):
    if p == r:
        return nums[p]
    q = partition(nums, p, r)
    k = q - p + 1
    if k == i:
        return nums[q]
    elif i < k:
        return select(nums, p, q - 1, i)
    return select(nums, q + 1, r, i - k)

def findKthLargest(nums, k):
    return select(nums, 0, len(nums) - 1, k)

def test():
    nums = [3,2,1,5,6,4]
    k = 3
    print findKthLargest(nums, k)
    nums = [-1, -1]
    k = 2
    print findKthLargest(nums, k)
    nums = [-1, 2, 0]
    k = 2
    print findKthLargest(nums, k)
    nums = [7,6,5,4,3,2,1]
    k = 2
    print findKthLargest(nums, k)
    nums = [2,1]
    k = 1
    print findKthLargest(nums, k)

test()