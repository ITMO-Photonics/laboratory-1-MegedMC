import scipy.optimize
import math
import time
def function(x):
	return math.cos(x) / (1 + x**2)
def derivative(x):
	return -math.sin(x) / (1 + x**2) - math.cos(x) / (1 + x**2)**2
print (scipy.optimize.bisect(function,0.1,2.4))
start_time = time.time()
for i in range(1000):
	scipy.optimize.bisect(function,0.1,2.4)
print("---Takes %s milliseconds for biesect method---" % (time.time() - start_time))

start_time = time.time()
for i in range(1000):
	scipy.optimize.newton(function,1.57, fprime = derivative)
print("---Takes %s milliseconds for Newton method with derivative---" % (time.time() - start_time))

start_time = time.time()
for i in range(1000):
	scipy.optimize.newton(function,1.57, fprime = None)
print("---Takes %s milliseconds for secant method---" % (time.time() - start_time))
start_time = time.time()
for i in range(1000):
	scipy.optimize.brentq(function,0.1,2.4)
print("---Takes %s millieconds for Brent method---" % (time.time() - start_time))
