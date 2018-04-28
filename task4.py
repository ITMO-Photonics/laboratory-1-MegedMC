import numpy
import scipy.linalg
import time
import matplotlib.pyplot as plt

A = numpy.random.random((150,150))
x = numpy.zeros((100,150))
b = numpy.zeros(150)
t = 0.0
start_time = time.time()
while (t<10.0):
	for  k in range (150):
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = scipy.linalg.solve(A,b)	
	print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for linalg-solve method---" % (time.time() - start_time))
######
t=0.0
lu,plv = scipy.linalg.lu_factor(A)
start_time = time.time()
while (t<10.0):
	for  k in range (150):
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = scipy.linalg.lu_solve((lu,plv),b)
	#print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for lu-decomposition method---" % (time.time() - start_time))
######
t=0.0
start_time = time.time()
Ainv=scipy.linalg.inv(A)
while (t<10.0):
	for  k in range (150):
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = numpy.dot(Ainv,b)
	#print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1
print("---Takes %s seconds for inverse-matrix method---" % (time.time() - start_time))