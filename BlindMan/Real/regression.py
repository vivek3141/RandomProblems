import random
import numpy as np
import matplotlib.pyplot as plt
def linearRegression(X,Y):
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    m = len(X)
    numer = 0
    denom = 0
    for i in range(m):
        numer += (X[i] - mean_x) * (Y[i] - mean_y)
        denom += (X[i] - mean_x) ** 2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)

    max_x = np.max(X) + 5
    min_x = np.min(X) - 5
    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x
    return b1, b0
def nonlinearRegression(X,Y):

X = []
Y = []
for i in range(11):
    X.append(random.randrange(10))
    Y.append(random.randrange(10))
linearRegression(X, Y)