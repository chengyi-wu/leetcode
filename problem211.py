def maximalSquare(matrix):
    row = len(matrix)
    col = len(matrix[0])
    square = 0
    for i in range(row):
        current = [0] * col
        for j in range(col):
            if i == 0:
                current[j] = int(matrix[i][j])
            elif j == 0:
                current[j] = int(matrix[i][j])
            else:
                if matrix[i][j] == '1' and matrix[i - 1][j - 1] == '1' :
                    current[j] = 0
                    for k in range(cache[j - 1] + 1):
                        if matrix[i - k][j] == '0' or matrix[i][j - k] == '0' or i - k < 0 or j - k < 0:
                            break
                        current[j] += 1
                else:
                    current[j] = int(matrix[i][j])
            square = max(current[j], square)
        cache = current
        print cache
    return square * square

def test():
    matrix = ["10100","10111","11111","10010"]
    #matrix = ["0001","1101","1111","0111","0111"]
    matrix = ["1111","1111","1111"]
    matrix = ["01101","11010","01110","11110","11111","00000"]
    print maximalSquare(matrix)

test()
