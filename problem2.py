
import numpy as np
import pandas as pd
import matplotlib as mpl
import argparse
import math


def scaler(X):
    """

    :param X:
    :return: a normalized version of X where the mean of each feature is 0 and the std is 1.
    """

    X_norm = X
    mean_vec = []
    std_vec = []

    for i in xrange(X.shape[1]):
        meanX = np.mean(X[:, i])
        stdX = np.std(X[:, i])
        mean_vec.append(meanX)
        std_vec.append(stdX)

        X_norm[:, i] = (X_norm[:, i] - meanX)/stdX

    return X_norm


def empRisk(w, X, y):
    """

    :param w: the weights to X, R^d
    :param X: input samples, age and weight
    :param y: the interpret, height
    :return: cost of the model
    """
    n = y.size
    y_pred = X.dot(w).flatten()
    sqr_error = (y_pred - y) ** 2

    risk = (1.0 / (2 * n)) * sqr_error.sum()

    return risk

def gradDescent(X, y, w, alpha = 0.001, iters = 100):
    """

    :param X:
    :param y:
    :param w:
    :param alpha:
    :param iters:
    :return:
    """
    n = y.size
    risks = np.zeros(shape = (iters, 1))

    for i in xrange(iters):
        y_pred = X.dot(w).flatten()
        w_size = w.size

        for wi in xrange(w_size):
            tmp = X[:, wi]
            m = tmp.shape[0]
            errorX = (y_pred - y) * tmp
            # update wi
            w[wi][0] = w[wi][0] - alpha * (1.0 / m) * errorX.sum()

        risks[i, 0] = empRisk(w, X, y)

    return w, risks






if __name__ == "__main__":

    # construct argument parser
    ap = argparse.ArgumentParser()
    ap.add_argument("dataInput", type=str, help="data set input for training.")
    ap.add_argument("dataOutput", type=str, help="output file as result")
    args = ap.parse_args()

    # input data set and prep
    trainData = pd.read_csv(args.dataInput, sep=',')
    X_raw = trainData.iloc[:, 0:-1].values
    y = trainData.iloc[:, -1].values
    n = X_raw.shape[0]
    X_intercept = np.ones(shape = (n, 1))
    X_norm = scaler(X_raw)
    X = np.concatenate((X_intercept, X_norm), axis = 1)

    # initialize weights, learning rate
    weights = np.zeros(shape= (X.shape[1], 1))
    alphas = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]

    # train and output result
    output2 = np.empty(shape=(1, X.shape[1]))
    for alpha in alphas:
        output = gradDescent(X, y, weights, alpha)[0].reshape((1, 3))
        output2 = np.concatenate((output2, output), axis = 0)

    # with my own choice of lr and iter
    res_own = gradDescent(X, y, weights, 0.01, 1000)
    output_own = res_own[0].reshape((1, 3))
    output2 = np.concatenate((output2, output_own), axis=0)[1:, :] #remove first initiation row
    #print(output2[0].reshape((1, 3)))
    df = pd.DataFrame(output2, columns=["b_0", "b_age", "b_weight"])

    df.to_csv(args.dataOutput, header=True, index=False, sep=',')







