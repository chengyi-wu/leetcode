def root(ids, i):
    while i != ids[i]:
        ids[i] = ids[ids[i]]
        i = ids[i]
    return i

def connected(ids, p, q):
    return root(ids, p) == root(ids, q)

def union(ids, p, q):
    i = root(ids, p)
    j = root(ids, q)
    ids[i] = j

def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    ids = [i for i in range(row * col)]

    opensites = []

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                x = i * col + j
                opensites.append(x)
                if i - 1 >= 0 and grid[i - 1][j] == '1':
                    y = (i - 1) * col + j
                    if not connected(ids, x, y):
                        union(ids, x, y)
                if i + 1 < row and grid[i + 1][j] == '1':
                    y = (i + 1) * col + j
                    if not connected(ids, x, y):
                        union(ids, x, y)
                if j - 1 >= 0 and grid[i][j - 1] == '1':
                    y = i * col + j - 1
                    if not connected(ids, x, y):
                        union(ids, x, y)
                if j + 1 < col and grid[i][j + 1] == '1':
                    y = i * col + j + 1
                    if not connected(ids, x, y):
                        union(ids, x, y)
    print opensites
    roots = []
    for s in opensites:
        r = root(ids, s)
        if r not in roots:
            roots.append(r)
    return len(roots)

def test():
    grid = ["11110","11010","11000","00000"]
    #grid = ["11000", "11000", "00100", "00011"]
    #grid = ["010","101","010"]
    print numIslands(grid)

test()
