####### Check Tree if they are identical using Queue ########

class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None
    

def CreateQueue(q, root):
    if root is not None:
        q.append(root)
        CreateQueue(q, root.left)
        CreateQueue(q, root.right)
    
    return q

def identical(root1,root2):
    que1=[]
    que2=[]
    que1=CreateQueue(que1 ,root1)
    que2=CreateQueue(que2, root2)

    while len(que1) or len(que2):
        value1=que1.pop(0)
        value2=que2.pop(0)

        if value1.key!=value2.key:
            return False

    return True

############### Using recursion because this will handle even trees with half nodes ######

def RecursionIdentical(root1, root2):

    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return RecursionIdentical(root1.left, root2.left) and RecursionIdentical(root1.right, root2.right)
    return False
    

root1=Node(1)
root1.left=Node(2)
root1.right=Node(3)

root2=Node(1)
root2.left=Node(2)
root2.right=Node(4)

print(RecursionIdentical(root1,root2))