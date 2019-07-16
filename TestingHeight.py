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

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(7)
root.left.right=Node(6)
root.right.left=Node(5)
root.right.right=Node(4)

print(treeHeight(root))
