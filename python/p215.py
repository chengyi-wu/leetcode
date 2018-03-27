def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A):
    '''
    Find the position of x in A
    '''
    x = A[-1] # change to random
    j = -1
    for i in range(len(A) - 1):
        if A[i] <= x:
            j += 1
            swap(A, i, j)
    j += 1
    swap(A, -1, j)
    return j

def select(A, i):
    '''
    Find the element that should be placed in A[i]
    '''
    if len(A) == 1:
        return A[0]
    k = partition(A)
    if i == k: # found it!
        return A[i]
    if k > i:
        return select(A[:k], i)
    return select(A[k:], i - k)

def findKthLargest(nums, k):
    i = len(nums) - k
    return select(nums, i)

print(findKthLargest([4,5,6,7], 4))
print('-----')
print(findKthLargest([7,6,5,4], 4))
print('-----')
print(findKthLargest([9,3,2,4,8], 3))