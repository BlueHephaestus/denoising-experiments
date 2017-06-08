import numpy as np
from scipy.sparse import csr_matrix

rows = []
cols = []
data = []
h = 2
w = 3

def ins(i, j, x):
    if j >= 0 and j < h*w:
        rows.append(i)
        cols.append(j)
        data.append(x)


for i in range(h*w):
    if i % w == w-1:
        ins(i, i-(w+1), 1)
        ins(i, i-(w), 1)
        ins(i, i-1, 1)
        ins(i, i+(w-1), 1)
        ins(i, i+(w), 1)

    elif i % w == 0:
        ins(i, i-(w), 1)
        ins(i, i-(w-1), 1)
        ins(i, i+1, 1)
        ins(i, i+(w), 1)
        ins(i, i+(w+1), 1)

    else:
        ins(i, i-(w+1), 1)
        ins(i, i-(w), 1)
        ins(i, i-(w-1), 1)
        ins(i, i-1, 1)
        ins(i, i+1, 1)
        ins(i, i+(w-1), 1)
        ins(i, i+(w), 1)
        ins(i, i+(w+1), 1)

rows = np.array(rows)
cols = np.array(cols)
data = np.array(data)

"""
Using our data and row and column indices, we create our adjacency matrix as a CSR Sparse matrix
"""
adjacency_matrix = csr_matrix((data, (rows, cols)), shape=(h*w, h*w))

"""
We then sum over all the rows of this matrix to get the degrees, 
    since it is a symmetric adjacency matrix this is the same as if we summed over the columns.

Once we have the degrees vector, we use it as the data to create a new sparse matrix, 
    of the same shape as our adjacency matrix, and with the vector elements on the diagonal
    via using (row, col) pairs of (0,0), (1,1), ..., (h*w-1, h*w-1) with (np.arange(h*w), np.arange(h*w))
"""
degrees = adjacency_matrix.sum(axis=1)
degrees = np.array(degrees).flatten()
degree_matrix = csr_matrix((degrees, (np.arange(h*w), np.arange(h*w))), shape=(h*w, h*w))

print adjacency_matrix.toarray()
print degree_matrix.toarray()
"""
We use the adjacency matrix and degree matrix to make our normalized adjacency matrix, via

    M = D^(-1/2) * A * D^(-1/2)

Where 
    D = degree matrix,
    A = adjacency matrix,
    M = normalized adjacency result

Since our degree matrix is a diagonal matrix, 
    the elementwise matrix power of it is the same 
    as the normal matrix power, so we can quickly 
    use the built-in csr_matrix function for elementwise power
    to compute D^(-1/2). 

We then do the dot product in the normal way.
"""
degree_matrix = degree_matrix.power(-1./2)
normalized_adjacency_matrix = degree_matrix.dot(adjacency_matrix.dot(degree_matrix))#(DA)D
print normalized_adjacency_matrix.toarray()
print np.sum(normalized_adjacency_matrix.toarray(), axis=1)

"""
now we need to get our y and choose a lambda and then solve for f
"""
