#PageRank with Teleportation, Power Iteration

import numpy as np
import pandas as pd

b = 0.8

graph_data = pd.read_csv('graph.txt', sep = '\t', header = None)
graph_data.columns = ['source', 'dest']
mat = graph_data.groupby(['source']).size().reset_index(name = 'cnt')
mat['deg'] = 1/mat['cnt']
cmat = pd.crosstab(graph_data['dest'], graph_data['source'])
n = len(cmat)

r = np.ones(n, dtype = np.float64) + 1/n

for m in cmat:
    d = mat[(mat['source'] == m)]['deg'].values[0]
    cmat[m] = cmat[m]*d

def compute_PR(b, cmat, r, n):
    for i in range(40):
        r = ((b*(cmat*r).sum(axis = 1)) + ((1-b)/n))
    return(r)

lowPR = np.argsort(compute_PR(b, cmat, r, n)) + 1
highPR = np.argsort(-compute_PR(b, cmat, r, n)) + 1

print("The top 5 node IDs with the highest PageRank scores: ", highPR[0:5])
print("The top 5 node IDs with the lowest PageRank scores: ", lowPR[0:5])




 



