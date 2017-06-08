import numpy as np

h = 4
w = 4

"""
for node i and node j to be neighbors
node j's h and w must be 1 or 0 away from node i's h and w, BUT NOT both 0 (this would be i itself)
    we could just delete the diagonal elements after if we want, but this wouldn't give us a row-by-row generation.

"""
adj = np.zeros((h*w, h*w), int)
i = 0
for row_i_i in range(h):
    for col_i_i in range(w):
        j = 0
        for row_i_j in range(h):
            for col_i_j in range(w):
                if row_i_i - row_i_j in [-1, 0, 1] and col_i_i - col_i_j in [-1, 0, 1] and not (row_i_i == row_i_j and col_i_i == col_i_j):
                    adj[i,j] = 1
                else:
                    adj[i,j] = 0




                j+=1
        i+=1
#print "  {}".format(np.arange(1,h*w+1))
"""
Raw print the matrix 
"""
for i,row in enumerate(adj):
    print ("%2i" % (i)), row

"""
Print row data per row
"""
"""
for i,row in enumerate(adj):
    neighbors = []
    for j,col in enumerate(row):
        if col == 1:
            neighbors.append(j)

    print ("%2i" % (i+1)), np.sum(row), np.array(neighbors)-(i+1)
"""



"""
for i in range(h*w):
    for j in range(h*w):
        check if i and j are neighbors
        check if i's h == j's h -1 or +1, 
        check if i's w == j's w -1 or +1
        if i == j-1
        print i+1
"""
