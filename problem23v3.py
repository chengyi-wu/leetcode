import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)

def mergeKLists(lists):
    '''
    :type lists: List[ListNode]
    :rtype ListNode
    Using Priority Queues to implement this. This is the preferred way.
    '''
    head = None
    p = None
    pq = []
    for n in lists:
        if n is not None:
            heapq.heappush(pq, (n.val, n))
    while len(pq) > 0:
        n = heapq.heappop(pq)[1]
        if n.next is not None:
            heapq.heappush(pq, (n.next.val, n.next))
        if head is None:
            head = n
        else:
            p.next = n
        p = n
    return head

def test():
    lists = [ListNode(0), ListNode(2), ListNode(3)]
    head = mergeKLists(lists)
    while head is not None:
        print head
        head = head.next
    
test()
