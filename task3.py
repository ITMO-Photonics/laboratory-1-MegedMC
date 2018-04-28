import numpy
import scipy.linalg
A = numpy.zeros((101,101))
i,j = numpy.indices(A.shape)
A[i==j+1]=1
A[i==j]=1
A[i==j+2]=1
B = numpy.arange(101)
print(scipy.linalg.solve(A,B))
print(A)
