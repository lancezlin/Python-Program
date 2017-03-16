import argparse
import numpy as np 
import pandas as pd 
from numpy.linalg import inv
from numpy import dot

class RidgeRegression(object):
	"""docstring for RidgeRegression"""


	def train(self, X, y, lamda):

		X = np.hstack((np.ones((X.shape[0], 1)), X))# add 1s col
		L = lamda * np.eye(X.shape([1]))
		L[0, 0] = 0
		self.w = dot(inv(dot(X.T, X) + L), dot(X.T, y))
		return self.w


	def predict(self, X):

		X = np.hstack((np.ones((X.shape[0], 1))), X)
		return dot(X, self.w)




if __name__ == "__main__":

	# import arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("lamda", type = str, help = "input the lamda for penalty.")
	ap.add_argument("sigma2", type = str, help = "input sigma sqr.")
	ap.add_argument("xTrain", type = str, help = "input training X data.")
	ap.add_argument("yTrain", type = str, help = "input train y data.")
	ap.add_argument("xTest", type = str, help = "input test data set.")
	args = ap.parse_args()


	# reading the datasets
	try:
		X_train = pd.read_csv(args.xTrain, sep = ",")
		X = X_train.iloc[:, :].values
	except:
		print("There is no training data available.")
		continue

	try:
		y_train = pd.read_csv(args.yTrain, sep = ",")
		y = y_train.iloc[:,:].values
	except:
		print("There is no training label available.")
		continue

	try:
		X_test = pd.read_csv(args.xTest, sep = ",")
		X_nod = X_test.iloc[:, :].values
	except:
		print("There is no x test data.")

	lamda = format(args.lamda, '.2f')
	sigma2 = format(args.sigma2, '.2f')


	# test out the model
	ridgeReg = RidgeRegression()
	wrr = ridgeReg.train(X, y, lamda)
	print(wrr)


