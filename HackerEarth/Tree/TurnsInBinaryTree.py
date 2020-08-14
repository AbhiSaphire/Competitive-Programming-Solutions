def findLCA(root, n1, n2): 
  
    # Base case 
    if root is None: 
        return None
    if root.data == n1 or root.data == n2: 
        return root 

    left_lca = findLCA(root.left, n1, n2) 
    right_lca = findLCA(root.right, n1, n2) 

    if left_lca and right_lca: 
        return root 

    return (left_lca if left_lca is not None else right_lca) 
  
def countTurn(root, key, turn): 
    global count 
    if root is None: 
        return False

    if root.data == key: 
        return True
  
    # Case 1: 
    if turn is True: 
        if countTurn(root.left, key, turn): 
            return True
        if countTurn(root.right, key, not turn): 
            count += 1
            return True
  
    # Case 2: 
    else: 
        if countTurn(root.right, key, turn): 
            return True
        if countTurn(root.left, key, not turn): 
            count += 1
            return True
    return False


def NumberOFTurns(root, first, second): 
    global count 
    LCA = findLCA(root, first, second) 
    if LCA is None: 
        return -1
  
    count = 0
  
    # case 1: 
    if LCA.data != first and LCA.data != second: 
        if countTurn(LCA.right, second, False) or countTurn( 
                LCA.left, second, True): 
            pass
        if countTurn(LCA.left, first, True) or countTurn( 
                LCA.right, first, False): 
            pass
        return count +1
  
    # case 2: 
    if LCA.data == first: 
        countTurn(LCA.right, second, False) 
        countTurn(LCA.left, second, True) 
        return count if count>0 else -1
    else: 
        countTurn(LCA.right, first, False) 
        countTurn(LCA.left, first, True) 
        return count if count>0 else -1