def reverse(ll):
    curr = ll
    forward = prev = None
    while curr != None:
        forward = curr.next
        curr.next = prev
        prev = curr
        curr = forward
    ll = prev
    return ll

def addLists(first, second):
    first = reverse(first)
    second = reverse(second)
    prev = None
    temp = None
    carry = 0 
    res = LinkedList()
    while(first is not None or second is not None): 
        fdata = 0 if first is None else first.data 
        sdata = 0 if second is None else second.data 
        Sum = carry + fdata + sdata 
        carry = 1 if Sum >= 10 else 0
        Sum = Sum if Sum < 10 else Sum % 10
        temp = Node(Sum) 

        if res.head is None: 
            res.head = temp 
        else : 
            prev.next = temp 

        prev = temp 

        if first is not None: 
            first = first.next
        if second is not None: 
            second = second.next
  
    if carry > 0: 
        temp.next = Node(carry)
    
    res.head = reverse(res.head)
    return res.head

# Input - 4 5, 3 4 5 || Output - 3 9 0
# Explanation - 
#           4->5
#        3->4->5
#        -------
#        3->9->0