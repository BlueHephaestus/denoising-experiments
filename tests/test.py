import numpy as np
from sklearn.feature_extraction.image import *

X = np.ones((2,3))
print img_to_graph(X).toarray()
"""
convert our h and w to an adjacency list
"""
print grid_to_graph(2, 3).toarray() - np.eye(3*2)
