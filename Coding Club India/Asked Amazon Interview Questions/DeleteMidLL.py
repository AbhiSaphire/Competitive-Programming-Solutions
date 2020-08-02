'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    if head == None or head.next == None:
        return None
        
    slow = fast = prev = head
    while slow and fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = slow.next
    
    return head