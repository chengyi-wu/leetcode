def maximalSquare(matrix):
    row = len(matrix)
    col = len(matrix[0])
    cache = []
    square = 0
    for i in range(row):
        cache.append([0] * col)
        for j in range(col):
            if i == 0:
                cache[i][j] = int(matrix[i][j])
            elif j == 0:
                cache[i][j] = int(matrix[i][j])
            else:
                if matrix[i][j] == '1' and matrix[i - 1][j - 1] == '1' :
                    cache[i][j] = 0
                    for k in range(cache[i - 1][j - 1] + 1):
                        if matrix[i - k][j] == '0' or matrix[i][j - k] == '0' or i - k < 0 or j - k < 0:
                            break
                        cache[i][j] += 1
                else:
                    cache[i][j] = int(matrix[i][j])
            square = max(cache[i][j], square)
        print cache[i]
        #print matrix[i]
    return square * square

def test():
    matrix = ["10100","10111","11111","10010"]
    #matrix = ["0001","1101","1111","0111","0111"]
    matrix = ["1111","1111","1111"]
    matrix = ["01101","11010","01110","11110","11111","00000"]
    print maximalSquare(matrix)

test()
