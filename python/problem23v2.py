def merge(l1, l2):
    head = None
    p1 = l1
    p2 = l2
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    p = None
    while p1 is not None or p2 is not None:
        if p1 is None:
            p.next = p2
            return head
        if p2 is None:
            p.next = p2
            return head
        
        if p1.val < p2.val:
            node = p1
            p1 = p1.next
        else:
            node = p2
            p2 = p2.next
        if head is None:
            head = node
        else:
            p.next = node
        p = node
    return head

def mergeKLists(lists):
    '''
    :type lists: List[ListNode]
    :rtype ListNode
    '''
    k = len(lists)
    while k > 1:
        l = lists.append(lists.pop(), lists.pop())
        k -= 1
    return lists[0]