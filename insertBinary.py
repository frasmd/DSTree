class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	
	def printTree(self, pnode):
		if(pnode!=None):
			print(pnode.data)
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
	
	def nodeDelete(self, pnode, key):
		pass

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
		
	def deleteDepestNode(self, pnode,d_node):
		q=[]
		q.append(pnode)
		while(len(q)):
			temp=q.pop(0)
			if temp is d_node:
				temp=None
				return
			if temp.right:
				if temp.right is d_node:
					temp.right=None
					return
				else:
					q.append(temp.right)
			
			if temp.left:
				if temp.left is d_node:
					temp.left=None
					return
				else:
					q.append(temp.left)
	
	def deleteKey(self, pnode, key):
		if pnode == None:
			return None

		if pnode.left == None and pnode.right == None:
			if pnode.data == key:
				return None
			else:
				return pnode
		key_node = None
		q = []
		q.append(pnode)
		while(len(q)):
			temp=q.pop(0)
			if temp.data==key:
				key_node=temp
			if temp.left:
				q.append(temp.left)
			if temp.right:
				q.append(temp.right)
			
		if key_node:
			x=temp.data
			self.deleteDepestNode(pnode, temp)
			key_node.data=x
		return pnode
node=Node(13)
node.left=Node(12)
node.right=Node(10)
node.left.left=Node(4)
node.left.right=Node(19)
node.right.left=Node(16)
node.right.right=Node(9)
node.printTree(node)
leftHeight=rightHeight=1
print("\n")
print("Height of tree is: " + str(node.heightOfTree(node,leftHeight,rightHeight)))

node.deleteKey(node,12)
node.printTree(node)
print("Height of tree is: " + str(node.heightOfTree(node,leftHeight,rightHeight)))