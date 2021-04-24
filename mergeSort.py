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


#MergeSort final Version
#Requires single extra array
#result arrary must be a duplicate of A

def mergeSort(A):
	copy=list(A)
	mergesort_array(copy, A, 0,len(A))


def mergesort_array(A, result, start, end):
	if end-start <2:
		return 
	if end-start==2:
		if result[start]>result[start+1]:
			result[start], result[start+1]=result[start+1], result[start]

		return 
	mid=(end+start)/2
	mergesort_array(result, A, start, mid)
	mergesort_array(result, A, mid, end)

	#merge
	i=start
	j=mid
	idx= start
	while idx<end:
		if j>= end or (i<mid and A[i]<A[j]):
			result [idx]=A[i]
			i+=1
		else:
			result[idx]=A[j]
			j+=1
		idx +=1








if __name__ =='__main__':
	x=[3,41,1,54,12]
	result=mergeSort(x)
	print(x)