def sortedInsert(current, data):
    '''
    current:  head of given sorted circular linked list
    data:  data to be inserted
    
    return: head of resultant circular linked list
    '''
    new_node = Node(data)
    if current is None: 
        new_node.next = new_node  
        return new_node

    head = current
    if (current.data >= new_node.data): 
        while current.next != head : 
            current = current.next
        current.next = new_node 
        new_node.next = head 
        head = new_node
        return head
        
    else: 
        while (current.next != head and 
            current.next.data < new_node.data): 
            current = current.next
  
        new_node.next = current.next
        current.next = new_node
        return head

# Input - 1 2 4, 2      || Output - 1 2 2 4
# Explanation - 
#   1->2->4  :: Since 2 (to be inserted value) is 2<=2<4
#   1->2->2->4