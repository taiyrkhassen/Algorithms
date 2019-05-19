class NodeBinaryTree:
    def init(self,data,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def init(self):
        self.root = None
    def getRoot(self):
        return self.root
    def insert(self,root = self.root,data):
        if self.root is None:
            root = NodeBinaryTree(data)
        else:
            if root.data < data:
                if root.right == None:
                    root.right = NodeBinaryTree(data)
                else:
                    self.insert(root = root.right, data)
            else:
                if root.left == None:
                    root.left = NodeBinaryTree(data)
                else:
                    self.insert(root = root.left, data)

def remove(self,root = self.root,data):
    if root is None:
        return None
    if data < root.data:
        root.left = remove(root = root.left, data)
    elif data > root.data:
        root.right = remove(root = root.right, data)
        else:
if root.left == None:
    temp = root.right
    root = None
    return temp
elif root.right == None:
    temp = root.left
    root = None
    return temp
temp = minValueNode(root.right)
root.data = temp.data
root.right = remove(root = root.right, temp.data)
