class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	
	def printTree(self, pnode):
		if(pnode!=None):
			print pnode.data,
			self.printTree(pnode.left)
			self.printTree(pnode.right)
	
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

	def insertTree(self, pnode, key):
		q=[]
		q.append(pnode)
		
		while(len(q)):
			#temp=q[0]	
			temp=q.pop(0)
			
			if(not temp.left):
				temp.left=Node(key)
				break
			else:
				q.append(temp.left)

			if(not temp.right):
				temp.right=Node(key)
				break
			else:
				q.append(temp.right)

	def deleteAnElement(self, pnode, delete):
		

		
node=Node(10)
node.left=Node(11)
node.right=Node(9)
node.left.left=Node(7)
node.right.left=Node(15)
node.right.right=Node(8)
node.printTree(node)
node.insertTree(node, 12)
print('\n')
print("Tree after raining:")
node.printTree(node)
leftHeight=rightHeight=1
print("\n")

print("Height of tree is: " + str(node.heightOfTree(node,leftHeight,rightHeight)))
