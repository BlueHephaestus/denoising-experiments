from scipy.sparse.linalg import *
import numpy as np

A = np.array([[3, 23, 9], [44, 7, 38], [5, 17, 37]])
B = np.array([[1, 2],[19, 4],[42, 6]])

X = np.zeros(B.shape, dtype=np.float32)
for i in range(B.shape[1]):
    b = B[:,i]
    b = np.reshape(b, (-1, 1))
    x, flags = bicg(A, b)
    X[:,i] = x

print np.dot(A, X)
print B

