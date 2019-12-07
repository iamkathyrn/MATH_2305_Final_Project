def incident_edges(G, T):
    edges = []
    for e in G[1]:
        for v in T[0]:
            if v in e and e not in T[1]:
                edges.append(e)
                
   #Remove edges that make cycles
                
    return edges

def cost(G,e):
    return G[1][e]

def initialize_tree(v):
    return(([v], []))
    
    
#add a min_cost_incident_edge(G, T)
################################################
def min_cost_incident_edge(G,T):
    edges = incident_edges(G,T)
    min_edges = edges[0]
    for i in range(1,len(edges)):
        if
        
        
    
        return min_e
#######################################################
#graph_cost returns the total weight of a graph
    
    
    ####prims algo########
#remove edges that make cycles
#make a function find a minimum edge
#return total edge cost of a given graph