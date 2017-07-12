class BST(object):
	class TreeNode(object):
		def __init__(self, k):
			self.key = k
			self.left = None
			self.right = None
		def __str__(self):
			return str(self.key)
			
	def __init__(self):
		self.root = None
		
	def rsearch(self, k, n):
		'''
		Recursive version of binary search
		'''
		if n == None:
			return None
		if n.key == key:
			return n
		if n.key < k:
			return self.search(k, n.right)
		else:
			return self.search(k, n.left)
			
	def search(self, k):
		'''
		Iterative version of binary search
		'''
		n = self.root
		while n!= None and n.key != k:
			if n.key < k:
				n = n.right
			else:
				n = n.left
				
		if n.key == k:
			return n
		return None
	
	def min(self):
		'''
		Iterative version
		'''
		n = self.root
		if n == None:
			return None
		while n.left != None:
			n = n.left
			
		return n
		
	def max(self):
		n = self.root
		if n == None:
			return None
		while n.right != None:
			n = n.right
		return n

	def rinsert(self, k, n = None):
		'''
		Recursive version of insert
		'''
		if n == None:
			if self.root == None:
				self.root = self.TreeNode(k)
				return
			return self.rinsert(k, self.root)
			
		if k > n.key:
			if n.right == None:
				n.right = self.TreeNode(k)
			else:
				self.rinsert(k, n.right)
		else:
			if n.left == None:
				n.left = self.TreeNode(k)
			else:
				self.rinsert(k, n.left)
				
	def insert(self, k):
		'''
		Iterative version of insert
		'''
		#print "insert", k
		parent = None
		n = self.root
		while n != None:
			parent = n
			if k > n.key:
				n = n.right
			else:
				n = n.left
		if parent == None:
			self.root = self.TreeNode(k)
		else:
			if k > parent.key:
				parent.right = self.TreeNode(k)
			else:
				parent.left = self.TreeNode(k)
				
	def traverse(self, n):
		if n == None:
			return
		self.traverse(n.left)
		print n,
		self.traverse(n.right)
		
		
	
	def delete(k):
		return
		
def test_BST():
	tree = BST()
	tree.insert(2)
	tree.insert(1)
	tree.insert(3)
	tree.insert(4)
	#print str(tree.root), str(tree.root.left), str(tree.root.right), str(tree.root.right.right)
	tree.traverse(tree.root)

test_BST()