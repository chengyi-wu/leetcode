class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def buildTree(preorder, inorder):
	#print preorder, inorder
	if len(preorder) == 0:
		return None
	if len(preorder) == 1:
		return TreeNode(preorder[0])
	n = TreeNode(preorder[0])

	i = inorder.index(preorder[0])

	leftInorder = inorder[:i]
	rightInorder = inorder[i + 1:]

	i = 1 + len(leftInorder)
	leftPreorder = preorder[1:i]
	rightPreorder = preorder[i:]

	n.left = buildTree(leftPreorder, leftInorder)
	n.right = buildTree(rightPreorder, rightInorder)

	return n

def InorderWalk(n):
	if n == None:
		return
	InorderWalk(n.left)
	print n.val,
	InorderWalk(n.right)

def PreorderWalk(n):
	if n == None:
		return
	print n.val,
	PreorderWalk(n.left)
	PreorderWalk(n.right)

def test_buildTree(preorder, inorder):
	n = buildTree(preorder, inorder)
	InorderWalk(n)
	print ""
	PreorderWalk(n)

test_buildTree([10,5,2,7,15,12], [2,5,7,10,12,15])
