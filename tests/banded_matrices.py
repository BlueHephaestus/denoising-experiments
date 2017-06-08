import numpy as np

def ins(adj, i, j, x):
    if j >= 0 and j < len(adj):
        adj[i,j] = x

tests = []
for h in range(20):
    print h
    for w in range(2,20):#Doesn't work with w == 1

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
                ins(adj, i, i+(w), 1)
                ins(adj, i, i+(w+1), 1)

            else:
                ins(adj, i, i-(w+1), 1)
                ins(adj, i, i-(w), 1)
                ins(adj, i, i-(w-1), 1)
                ins(adj, i, i-1, 1)
                ins(adj, i, i+1, 1)
                ins(adj, i, i+(w-1), 1)
                ins(adj, i, i+(w), 1)
                ins(adj, i, i+(w+1), 1)

        adj2 = adj

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

        """
        for i in range(h*w):
            print i, adj2[i], np.all(adj2[i] == adj[i]), i % w
            print i, adj[i]
            print ""
        """

        #print np.all(adj2==adj)
        if not np.all(adj2==adj):
            for i in range(h*w):
                print i, adj2[i], np.all(adj2[i] == adj[i]), i % w, h, w
                print i, adj[i]
                print ""
        tests.append(np.all(adj2==adj))
"""
for i,row in enumerate(adj):
    print ("%2i" % (i+1)), row
"""
tests = np.array(tests)
print np.all(tests)
