# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    '''
    :type lists: List[ListNode]
    :rtype ListNode
    '''
    head = None
    p = None
    lists = [l for l in lists if l is not None]
    k = len(lists)
    while k > 0:
        node = None
        pos = -1
        for i in xrange(k):
            n = lists[i]
            if node is None:
                node = n
                pos = i
            elif n.val < node.val:
                node = n
                pos = i
        lists[pos] = node.next
        if head is None:
            head = node
        else:
            p.next = node
        p = node
        if lists[pos] is None:
            lists.remove(None)
            k -= 1
    return head

