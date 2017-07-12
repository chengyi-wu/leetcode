def islandPerimeter(grid):
	nRow = len(grid)
	nCol = len(grid[0])
	p = 0
	for i in range(nRow):
		for j in range(nCol):
			v = 0
			if grid[i][j] == 1:
				if i == 0:
					v += 1
					if i + 1 < nRow and grid[i + 1][j] == 0:
						v += 1
				if j == 0:
					v += 1
					if j + 1 < nCol and grid[i][j + 1] == 0:
						v += 1
				if i == nRow - 1:
					v += 1
					if grid[i - 1][j] == 0:
						v += 1
				if j == nCol - 1:
					v += 1
					if grid[i][j - 1] == 0:
						v += 1
				if i > 0 and i < nRow - 1:
					if grid[i - 1][j] == 0:
						v += 1
					if grid[i + 1][j] == 0:
						v += 1
				if j > 0 and j < nCol - 1:
					if grid[i][j - 1] == 0:
						v += 1
					if grid[i][j + 1] == 0:
						v += 1
			print v,
			p += v
		print ""
	return p

def test_islandPerimeter(grid):
	print grid
	print islandPerimeter(grid)

test_islandPerimeter([[1,0,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])

test_islandPerimeter([[1]])