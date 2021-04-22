#Binary Search File

from time import time



def contains(collection, target):
	return target in collection


#Binary Search Code
def bs_contains(ordered, target):
	low=0
	high=len(ordered)-1
	while low<=high:
		mid=(low+high)/2
		if target==ordered[mid]:
			return True
		elif target < ordered[mid]:
			high =mid-1

		else:
			low =mid+1
	return False

#uses Binary Search to return the target value
def bs_contains(ordered, target):
	low=0
	high=len(ordered)-1
	while low<=high:
		mid=(low+high)/2
		if target==ordered[mid]:
			return mid
		elif target < ordered[mid]:
			high =mid-1

		else:
			low =mid+1
	return -(low+1)


def insertInPlace2(ordered, target):
	idx= bs_contains(ordered, target)
	if idx<0:
		ordered.insert(-(idx+1), target)
		return 

	ordered.insert(idx,target)

#///////////// measuring performance of program	

# inserting at particular place using normal method
def insertInPlace(ordered, target):
	for i in range(len(ordered)):
		if target<ordered[i]:
			ordered.insert(i,target)
			return 

		ordered.append(target)

#///////////// measuring performance of program


def performance():
	n=1024
	while n<50000000:
		sorted=range(n)
		now=time()

		insertInPlace2(sorted, n+1)
		done=time()
		print(n, (done-now)*1000)
		n*=2



if __name__ =='__main__':
	performance()