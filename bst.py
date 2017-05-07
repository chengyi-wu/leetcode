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
		print "insert", v
		node = TreeNode(v)
		
		if self.root == None:
			self.root = node
			return
		
		parent = self.root
		while parent.left != None or parent.right != None:
			if parent.val < v:
				parent = parent.right
				print parent
			else:
				parent = parent.left
				print parent
		
		if parent.val < v:
			parent.right = node
		else:
			parent.left = node
		
			
	def getRoot(self):
		return self.root
		
def preOrder(n):
	if n.left != None:
		preOrder(n.left)
	if n.right != None:
		preOrder(n.right)
	print n
		
		
			
def testBST():
	t = Tree()
	for i in range(1,5):
		t.insert(i)
	print t.root, t.root.left, t.root.right
	preOrder(t.root)

testBST()