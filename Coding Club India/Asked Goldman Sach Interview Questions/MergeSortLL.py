def split(tempHead): 
    fast = slow = tempHead 
    while(True): 
        if fast.next is None: 
            break
        if fast.next.next is None: 
            break
        fast = fast.next.next 
        slow = slow.next
              
    temp = slow.next
    slow.next = None
    return temp
    
def merge(first, second): 
          
    # If first linked list is empty 
    if first is None: 
        return second  
          
    # If secon linked list is empty  
    if second is None: 
        return first 
  
    # Pick the smaller value 
    if first.data < second.data: 
        first.next = merge(first.next, second) 
        first.next.prev = first 
        first.prev = None   
        return first 
    else: 
        second.next = merge(first, second.next) 
        second.next.prev = second 
        second.prev = None
        return second
        
def sortDoubly(tempHead):
    if tempHead is None:  
        return tempHead 
    if tempHead.next is None: 
        return tempHead 
          
    second = split(tempHead) 
          
    # Recur for left and righ halves 
    tempHead = sortDoubly(tempHead) 
    second = sortDoubly(second) 
  
    # Merge the two sorted halves 
    return merge(tempHead, second)