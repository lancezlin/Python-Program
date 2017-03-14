#
#

import numpy as np
import pandas as pd
import matplotlib as mpl
import argparse
import math



# activation function
def signX(x):
    """ return 1 if x>=0, -1 otherwise
    """
    return math.copysign(1, x)

def classifier(w, b, s):
    """
    :param w: the weights vector from input
    :param b: the bias vector
    :param s: sample data
    :return: class label based on the sign function
    """
    return signX(sum(wi * si for wi, si in zip(w, s)) + b)

def train(samples, labels, iters = 200, alpha = 0.01):
    """
    :param samples: features input - X
    :param labels: label vector - y
    :param iters: maximum iterations, default 200
    :param alpha: the learning rate of the algo, default 0.1
    :return: the trace of the weights and bias
    """
    dims = samples.shape[1]
    weights = [0] * dims
    b = 0
    output = np.array([])
    for i in xrange(iters):
        err = 0
        for sample, label in zip(samples, labels):
            if classifier(weights, b, sample) != label:
                weights = [weight + (alpha * label * feature) for weight, feature in zip(weights, sample)]
                b += alpha * label
                err += 1
                #print(np.concatenate((output, np.array(weights)), axis = 0))
                output = np.concatenate((output, np.append(weights, b)))
        if err == 0:
            break
        #np.vstack((output, np.asanyarray(weights.append(b))))
    output1 = np.reshape(output, (-1, 3))
    return output1


if __name__ == "__main__":
    # construct argument parser
    ap = argparse.ArgumentParser()
    ap.add_argument("dataInput", type=str, help="data set input for training.")
    ap.add_argument("dataOutput", type=str, help="output file as result")
    args = ap.parse_args()

    # input data set
    trainData = pd.read_csv(args.dataInput, sep=',')
    X = trainData.iloc[:, 0:-1].values
    y = trainData.iloc[:, -1].values

    # train and output result
    output1 = train(X, y)
    df = pd.DataFrame(output1, columns=["w_1", "w_2", "b"])
    df.to_csv(args.dataOutput, header=True, index=False, sep=',')


    #np.savetxt(args.dataOutput, output1, delimiter= ",")



