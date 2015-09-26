import numpy as np
import numpy.linalg as la


# 
def linearKernel(x1, x2):
	return np.dot(x1, x2)

def polynomialKernel(x, y, p=3):
	return (1 + np.dot(x, y))**p

def gaussianKernel(x, y, sigma=5.0):
	return np.exp(-la.norm(x-y)**2 / (2 * (sigma ** 2)))



