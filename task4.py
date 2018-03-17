import numpy
import scipy.linalg
import matplotlib.pyplot as plt

A = numpy.random.random((50,50))
x = numpy.zeros((100,50))
b = numpy.zeros(50)
t = 0.0
while (t<10.0):
	for  k in range (50):	
		b[k] = k/(1+ k * t)
	x[int(t*10)][:] = scipy.linalg.solve(A,b)	
	print(numpy.linalg.norm(x[int(t*10)][:],ord=2))
	t=t+0.1

