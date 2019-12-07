#prims goes here
from functions.graph_operations import min_cost_incident_edge, initialize_tree
from functions.reading_writing_functions import get_graph

def prims(textfile):
    G = get_graph(textfile)
    T = initialize_tree(G, v)
    
    while T[0] != G[0]:
        e = min_cost_incident_edge(G, T)
        #e = min_cost_edge(G, T)
        #add e and its verticies to T.....
        #######################################
        T[1].append(e)
        T[0].append(e[0])
        T[1].append(e[1])
        #########################################
        
    return T