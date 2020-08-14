def storeBSTNodes(root,nodes):
    if not root: 
        return
    storeBSTNodes(root.left,nodes) 
    nodes.append(root) 
    storeBSTNodes(root.right,nodes) 
    
def buildTreeUtil(nodes,start,end):
    if start > end: 
        return None
    mid = (start + end) // 2
    node = nodes[mid] 
    node.left = buildTreeUtil(nodes,start,mid-1) 
    node.right = buildTreeUtil(nodes,mid+1,end) 
    return node 

def buildBalancedTree(root): 
    nodes = [] 
    storeBSTNodes(root,nodes) 
    n = len(nodes) 
    return buildTreeUtil(nodes,0,n-1)