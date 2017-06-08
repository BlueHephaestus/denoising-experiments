import numpy as np

def ins(adj, i, j, x):
    if j >= 0 and j < len(adj):
        adj[i,j] += x

h = 300
w = 400

adj = np.zeros((h*w, h*w), int)

for i in range(h*w):
    if i % w == w-1:
        ins(adj, i, i-(w+1), 1)
        ins(adj, i, i-(w), 1)
        ins(adj, i, i-1, 1)
        ins(adj, i, i+(w-1), 1)
        ins(adj, i, i+(w), 1)

    elif i % w == 0:
        ins(adj, i, i-(w), 1)
        ins(adj, i, i-(w-1), 1)
        ins(adj, i, i+1, 1)
        ins(adj, i, i+(w-1), 1)
        ins(adj, i, i+(w), 1)

    else:
        ins(adj, i, i-(w+1), 1)
        ins(adj, i, i-(w), 1)
        ins(adj, i, i-(w-1), 1)
        ins(adj, i, i-1, 1)
        ins(adj, i, i+1, 1)
        ins(adj, i, i+(w-1), 1)
        ins(adj, i, i+(w), 1)
        ins(adj, i, i+(w+1), 1)


