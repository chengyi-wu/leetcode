def kthSmallest(matrix, k):
    '''
    Convert the matrix to 1D array, sort the array and return the value
    '''
    row = len(matrix)
    col = len(matrix[0])
    #list comprehension is much faster
    nums = [(matrix[i][j], i * col + j ) for i in range(row) for j in range(col)]
    nums.sort(key=lambda x:x[0])
    
    n = nums[k - 1][1]
    y = n % col
    x = (n - y) // col
    return matrix[x][y]