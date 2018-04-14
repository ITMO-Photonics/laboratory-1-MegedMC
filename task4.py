import numpy
import scipy.linalg
import time
import matplotlib.pyplot as plt

A = numpy.random.random((50,50))
x = numpy.zeros((100,50))
b = numpy.zeros(50)
t = 0.0
start_time = time.time()
while (t<10.0):
	for  k in range (50):	
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = scipy.linalg.solve(A,b)	
	print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for linalg-solve method---" % (time.time() - start_time))
######
t=0.0
start_time = time.time()
while (t<10.0):
	for  k in range (50):
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = scipy.linalg.lu_solve(scipy.linalg.lu_factor(A),b)
	#print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for lu-decomposition method---" % (time.time() - start_time))
######
t=0.0
start_time = time.time()
while (t<10.0):
	for  k in range (50):
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = numpy.matmul(scipy.linalg.inv(A),b)
	#print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for inverse-matrix method---" % (time.time() - start_time))