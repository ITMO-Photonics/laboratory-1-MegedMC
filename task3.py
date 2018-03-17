import numpy
import scipy.linalg
A = numpy.zeros((101,101))
i,j = numpy.indices(A.shape)
A[i==j+1]=1
A[i==j]=1
A[i==j+2]=1
B = numpy.zeros(101)
for i in range(101):
	B[i] = i
print(scipy.linalg.solve(A,B))
