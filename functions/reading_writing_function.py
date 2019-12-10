import numpy as np

def get_graph(textfile):
    
    #gets data from .txt file
    edgelist = np.loadtxt(f'data/{textfile}', dtype = int )
    
    #([],{}) ...[NODES], {EDGES:WEIGHT}
    G = ([],{})

    for x in edgelist:

        if x[0] not in G[0]:
            G[0].append(x[0])

        if x[1] not in G[0]:
            G[0].append(x[1])
        
        #converting data to dictionary
        G[1][(x[0], x[1])] = x[2]

    return G