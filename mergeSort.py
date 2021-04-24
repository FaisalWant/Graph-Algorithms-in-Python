#inefficient merge sort
#extra space needed

def copymergesort(A):
	if len(A)<2:
		return A

	mid=len(A)/2
	left= copymergesort(A[:mid])
	right=copymergesort(A[mid:])
	i=j=0
	B=[]


	while len(B)<len(A):
		if j>=len(right) or ( i< mid and left[i]<right[j]):
			B.append(left[i])
			i+=1
		elif j<len(right):
			B.append(right[j])
			j+=1
	return B



if __name__ =='__main__':
	x=[3,41,1,54,12]
	result=copymergesort(x)
	print(result)