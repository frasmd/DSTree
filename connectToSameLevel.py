class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None
        self.nextRight=None


def connectNext(root):

    que=[]
    que.append(root)
    que.append(None)

    while que:
        temp=que.pop(0)
        if temp != None:
            temp.nextRight=que[0]
            if temp.left:
                que.append(temp.left)
            if temp.right:
                que.append(temp.right)
        elif que:
            que.append(None)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(7)
root.right.right=Node(4)

connectNext(root)



        