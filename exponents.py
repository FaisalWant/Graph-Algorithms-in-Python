import numpy
import random



def exponent(x,n):
	if n==0:
		return 1
	if n==1:
		return x

	if n%2:
		return x*exponent(x*x, (n-1)/2)

	return exponent(x*x, n/2)


def exponent_mod(x,n,m):
	if n==0:
		return 1
	if n==1:
		return x%m

	if n%2:
		return x*exponent_mod(x*x%m, ((n-1)/2)%m, m)

	return exponent_mod(x*x, n/2, m)%m	

#matrix exponent
def randomMatrix(n):

	r=[]
	for i  in range(n):
		r.append([random.random() for i in range(n)])
	base= numpy.array(r).reshape((n,n))

	return base



# recursive case for multiplying matrices

def exponent_mat(x,n):
	# n is raised by power
	if n==0:
		return numpy.identity(len(x))
	if n==1:
		return x

	if n%2:
		return x.dot(exponent(x.dot(x), (n-1)/2))

	return exponent_mat(x.dot(x), n/2)


# non recursive verion of exponent multiplication

def exponent_nonr(x,n):
	if n==0:
		return 1
	if n==1:
		return x
	val=1
	while n>0:
		if n%2:
			val*=x
			n-=1
		n/=2
		if n>0:
			x*=x


	return val



if __name__ =='__main__':
	m= randomMatrix(3)
	print(m)
	# print("Squard result")

	print(exponent_mat(m,2))



