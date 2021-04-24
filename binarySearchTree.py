
#BinarySearch Tree Implementation
import random
from time import time

class BinaryNode:
	
	def __init__(self, value=None):
		self.value=value
		self.left=None
		self.right=None

	def add(self,val):
		if val<=self.value:
			if self.left:
				self.left.add(val)
			else:
				self.left=BinaryNode(val)
		else:
			if self.right:
				self.right.add(val)

			else:
				self.right=BinaryNode(val)

	def delete(self):
		if self.left==self.right==None:
			return None

		if self.left==None:
			return self.right
		if self.right==None:
			return self.left

		child=self.left
		grandchild=child.right
		if grandchild:
			while grandchild.right:
				child=grandchild
				grandchild=child.right
			self.value=grandchild.value
			child.right=grandchild.left

		else:
			self.left=child.left
			self.value=child.value

		return self



class BinaryTree:
	def __init__(self):
		self.root=None

	def add(self, value):

		if self.root is None:
			self.root= BinaryNode(value)

		else:
			self.root.add(value)

	def contains(self,target):
		node=self.root
		while node:
			if target==node.value:
				return True
			if target<node.value:
				node=node.left
			else:
				node= node.right	

		return False	

	def remove(self, value):
		if self.root:
			self.root=self.removeFromParent(self.root, value)

	def removeFromParent(self, parent, value):
		if parent is None:
			return None

		if value==parent.value:
			return parent.delete()
		elif value<parent.val:
			parent.left=self.removeFromParent(parent.left, value)
		else:
			parent.right=self.removeFromParent(parent.right, value)
		return parent

	



def perfomance():
	n=1024
	while n<=65516:
		bt=BinaryTree()
		for i in range(n):
			bt.add(random.randint(1,n))

		now= time()
		bt.contains(random.randint(1,n))
		print(n,(time()-now)*1000)
		n*=2


# if __name__ =='__main__':
# 	bt=BinaryTree()
# 	bt.add(5)
# 	bt.add(10)
# 	bt.add(7)
# 	bt.add(2)
# 	bt.add(1)
# 	bt.add(8)
# 	print(bt.contains(5))
# 	print(bt.contains(50))
# 	bt.remove(5)
# 	print(bt.contains(5))