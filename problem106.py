class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.val)

def buildTree(inorder, postorder):
	#print inorder,postorder
	if len(postorder) == 0:
		return None
	if len(postorder) == 1:
		return TreeNode(postorder[0])
	n = TreeNode(postorder[-1])

	i = inorder.index(postorder[-1])

	leftInorder = inorder[:i]
	rightInorder = inorder[i + 1:]

	#print leftInorder, rightInorder

	i = len(leftInorder)
	leftPostorder = postorder[:i]
	rightPostorder = postorder[i:-1]

	#print leftPostorder, rightPostorder

	n.left = buildTree(leftInorder, leftPostorder)
	n.right = buildTree(rightInorder, rightPostorder)

	return n

def InorderWalk(n):
	if n == None:
		return
	InorderWalk(n.left)
	print n,
	InorderWalk(n.right)

def PostorderWalk(n):
	if n == None:
		return
	PostorderWalk(n.left)
	PostorderWalk(n.right)
	print n,

def test_buildTree(preorder, inorder):
	n = buildTree(preorder, inorder)
	#InorderWalk(n)
	#print ""
	#PostorderWalk(n)
	#print ""

test_buildTree([2,5,7,10,12,15],[2,7,5,12,15,10])
