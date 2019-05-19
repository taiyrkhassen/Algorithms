class Node: 
    def __init__(self,key): 
        self.data = key
        self.left = None
        self.right = None
     
  
  
 
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root != None: 
  
        # First print the data of node 
        print(root.data), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left = Node(3) 
root.right  = Node(8)
root.right.right  = Node(9)
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

print ("Preorder traversal of binary tree is")
printPreorder(root) 
  
