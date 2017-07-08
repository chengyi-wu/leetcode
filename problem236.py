# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root, p, q):
    '''
    BFS for the tree using parent pointers.
    Get the root to p,q pathes and find the LCA.
    This is general algorithm and can be used to solve RMQ problems. 
    Build the tree in O(N) time or O(nlogn) time.
    '''
    parent = {root:None}
    frontier = [root]
    while len(frontier) > 0:
        next = []
        for n in frontier:
            left = n.left
            right = n.right
            if left is not None:
                next.append(left)
                parent[left] = n
            if right is not None:
                next.append(right)
                parent[right] = n
        frontier = next
    
    #find the root to p and q's path.
    pPath = []
    qPath = []
    x = p
    while x is not None:
        pPath.append(x)
        x = parent[x]
    x = q
    while x is not None:
        qPath.append(x)
        x = parent[x]
    pPath = pPath[::-1]
    qPath = qPath[::-1]
    
    size = min(len(pPath), len(qPath))

    x = 0
    while x < size and pPath[x] == qPath[x]:
        x += 1
    return pPath[x - 1]
    