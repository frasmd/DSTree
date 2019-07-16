class Node:
    def __init__(self, key=None):
        self.key=key
        self.right=None
        self.left=None

def treeHeight(root):

    if root is None:
        return 0
    lheight=treeHeight(root.left)
    rheight=treeHeight(root.right)
    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1

def LevelPrint(root, level, printOrder):

    if root is None:
        return 
    if level==1:
        print(root.key, end=' ')
    elif(level > 1):
        if(printOrder):
            LevelPrint(root.left, level-1, printOrder)
            LevelPrint(root.right, level-1, printOrder)
        else:
            LevelPrint(root.right, level-1, printOrder)
            LevelPrint(root.left, level-1, printOrder)

def printSpiral(root):
    height=treeHeight(root)

    printOrder=0

    for i in range(1, height+1):
        LevelPrint(root, i, printOrder)

        printOrder= not printOrder

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(7)
root.left.right=Node(6)
root.right.left=Node(5)
root.right.right=Node(4)

printSpiral(root)