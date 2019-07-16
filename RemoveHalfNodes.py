######################  Remove Half nodes from a binary treee ##########################
class Node:
    def __init__(self, key=None):
        self.key=key
        self.right=None
        self.left=None

    def heightOfLeftTree(self, pnode, leftHeight):
        if(pnode.left):
            leftHeight+=1
            self.heightOfLeftTree(pnode.left, leftHeight)
        return leftHeight
    
    def heightOfRightTree(self, pnode, rightHeight):
        if(pnode.right):
            rightHeight+=1
            self.heightOfRightTree(pnode.right, rightHeight)
        return rightHeight

    def heightOfTree(self,pnode,leftHeight,rightHeight):
        return max(self.heightOfLeftTree(pnode,leftHeight),self.heightOfRightTree(pnode, rightHeight))+1

    def printTree(self, pnode):
    	if(pnode!=None):
    		print(pnode.key)
    		self.printTree(pnode.left)
    		self.printTree(pnode.right)

def levelOrderEfficient(node):
    q=[]
    q.append(node)
    if node==None:
        return
    
    while len(q):
        out_node=q.pop(0)
        print(out_node.key)

        if out_node.left != None:
            q.append(out_node.left)
        if out_node.right != None:
            q.append(out_node.right)

def deleteHalfNodes(pnode):
    if pnode is None:
        return None
    pnode.left = deleteHalfNodes(pnode.left)
    pnode.right=deleteHalfNodes(pnode.right)

    if pnode.left is None and pnode.right is None:
        return pnode
    if pnode.left is None:
        replacement=pnode.right
        temp=pnode
        pnode=None
        del(temp)
        return replacement
    if pnode.right is None:
        replacement=pnode.left
        temp=pnode
        pnode=None
        del(temp)
        return replacement
    return pnode


def checkFullTree(node):
    if node==None:
        return True ## 0 nodes is a binary full tree
    if (node.left is not None and node.right is None) or (node.left is None and  node.right is not None):
        return False
    
    return checkFullTree(node.left) and checkFullTree(node.right) ### Both subtrees should be full trees


node=Node(1)
node.left=Node(2)
node.right=Node(3)
node.left.left=Node(4)
node.left.right=Node(6)
node.right.left=Node(7)
node.right.right=Node(5)
print(checkFullTree(node))