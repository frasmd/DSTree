####### Size of Binary Tree using Queue ########
import time
class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

def Size(root):
    q=[]
    q.append(root)
    count=0
    while(len(q)):
        value=q.pop(0)
        count+=1
        if value.left is not None:
            q.append(value.left)
        if value.right is not None:
            q.append(value.right)
    return count

####### Size of Binary Tree using Recursion ########

def recursionSize(root):
    if not root:
        return 0
    return 1+recursionSize(root.left)+recursionSize(root.right)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(60)

starttime=time.time()
print(Size(root))   
print("With Queue" + str(time.time()-starttime))

starttime=time.time()
print(recursionSize(root))   
print("With Recursion" + str(time.time()-starttime))
