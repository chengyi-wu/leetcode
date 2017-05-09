class TreeNode(object):
		def __init__(self, v):
			self.val = v
			self.left = None
			self.right = None
		def __str__(self):
			return str(self.val)

class Tree(object):
	def __init__(self):
		self.root = None
	def insert(self, v):
		#print "insert", v
		node = TreeNode(v)
		
		parent = None
		n = self.root
		while n != None:
			parent = n
			if v > n.val:
				n = n.right
			else:
				n = n.left
				
		if parent == None:
			self.root = node
		else:
			#print parent
			if v > parent.val:
				parent.right = node
			else:
				parent.left = node
		
			
	def getRoot(self):
		return self.root
		
def inOrder(root):
	n = root

		

def isValidRightChild(path, node):
	i = len(path) - 1
	n = node
	parent = path[i]
	while i > 0 and n != parent.left:
		i -= 1
		n = parent
		parent = path[i]
	return node.right.val < parent.val
	
def isValidBSTHelper(path, n):
	#print "checking", str(n)
	leftValid = True
	rightValid = True
	
	#check the left & right children
	if n.left != None:
		if n.left.val > n.val:
			leftValid = False
		else:
			leftValid = isValidBSTHelper(path + [n], n.left)
	
	if n.right != None:
		if n.right.val < n.val:
			rightValid = False
		else:
			rightValid = isValidBSTHelper(path + [n], n.right)
			
	if (leftValid and rightValid) == False:
		print "EARLY VIOLATION!!!"
		return False
	#check the path for violation
	i = len(path) - 1
	while i > 0:
		if path[i] == path[i - 1].left and n.val >= path[i - 1].val:
			print "VIOLATING!!!",  n.val, path[i-1].val
			return False
		if path[i] == path[i - 1].right and n.val <= path[i - 1].val:
			print "VIOLATING!!!", n.val, path[i-1].val
			return False
		i -= 1
	
	return True
	
def isValidBST(root):
	if root == None:
		return True
	leftValid = True
	rightValid = True
	if root.left != None:
		if root.val <= root.left.val:
			return False
		leftValid = isValidBSTHelper([root], root.left)
	if root.right != None:
		if root.val >= root.right.val:
			return False
		rightValid = isValidBSTHelper([root], root.right)
	return leftValid and rightValid
		
			
def testBST():
	root = TreeNode(10)
	root.left = TreeNode(5)
	root.left.left = TreeNode(1)
	root.right = TreeNode(15)
	root.right.left = TreeNode(2)
	root.right.right = TreeNode(20)
	
	print isValidBST(root)
	
def testBST2():
	root = TreeNode(3)
	root.left = TreeNode(1)
	root.right = TreeNode(5)
	root.left.left = TreeNode(0)
	root.left.right = TreeNode(2)
	root.left.right.right = TreeNode(3)
	#root.right.right = TreeNode(20)
	
	print isValidBST(root)
	
	
import cProfile
cProfile.run('testBST()')
cProfile.run('testBST2()')