import time

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

def leverordertraversal(node):
    h=Node()
    leftHeight=rightHeight=1
    height=0
    height=h.heightOfTree(node, leftHeight, rightHeight)

    for i in range(1, height+1):
        NodesAtALevel(node, i)

def NodesAtALevel(node, i):
    if node is None:
        return
    if i==1:
        print(node.key, end=' ')
    elif i>1:
        NodesAtALevel(node.left, i-1)
        NodesAtALevel(node.right, i-1)

def levelOrderEfficientLineByLine(node):
    if node==None:
        return
    q=[]
    q.append(node)
    q.append(None)
    while len(q) > 1:
        out_node=q.pop(0)
        if out_node == None:
            q.append(None)
            print("$", end=' ')
        else:
            if out_node.left != None:
                q.append(out_node.left)
            if out_node.right != None:
                q.append(out_node.right)
            
            print(out_node.key, end=' ')
    print("$", end=' ')     

def ReverselevelOrderEfficient(node):
    if node==None:
        return
    q=[]
    result=[]
    q.append(node)
    while len(q):
        out_node=q.pop(0)
        result.append(out_node.key)
        if out_node.left != None:
            q.append(out_node.left)
        if out_node.right != None:
            q.append(out_node.right)
    while(len(result)):
        print(result.pop(), end=' ')

pnode = Node(1) 
pnode.left = Node(2) 
pnode.right = Node(3) 
pnode.left.left = Node(4) 
pnode.left.right = Node(5) 

ReverselevelOrderEfficient(pnode)

