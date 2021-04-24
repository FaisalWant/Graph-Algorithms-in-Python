#Balanced BinarySearch tree from a sorted list
#overcomming the skew problem
#usng median heruistic

#advance Python is the current directory

from advancePython.binarySearchTree import BinaryTree

def balancedTree(ordered):
	bt=BinaryTree()
	addRange(bt, ordered, 0,len(ordered)-1)
	return bt


def addRange(bt, ordered, low, high):

	if low<=high:
		mid=(low+high)/2
		bt.add(ordered[mid])
		addRange(bt, ordered, low, mid-1)
		addRange(bt, ordered, mid+1, high)


if __name__ =='__main__':
	x=range(10)
	bt=balancedTree(x)
	print(bt.root.value)