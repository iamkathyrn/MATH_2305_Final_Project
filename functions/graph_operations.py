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
    
    
    
    
    def min_cost_incident_edge(G, T):
    
    inedges = incident_edges(G, T)  #get incident edges
    min, returnedge = cost(G, inedges[0]), inedges[0] #starting minimum and return edge
    for e in inedges:  #loop through incident edges
        edgecost = cost(G, e)
        if edgecost < min:  #if cost is smaller than minimum
            min = edgecost  #set minimum
            returnedge = e  #set return
        
    return returnedge

    
def add_new_edge(G, T):
     
     newedge = min_cost_incident_edge(G, T)
     T[1].append(newedge)
     for v in newedge: 
          if v not in T[0]:
              T[0].append(v)
        
     return T
   
# checks tree to see if it's path has been completed
def check_tree(G, T):
    
    g_len = len(G[0])
    t_len = len(T[0])
    
    if g_len == t_len:
        return 1
    else:
        return 0    
  
def tree_cost(G,T): # finds edgecost of tree
    treecost = 0
    for e in T[1]:
        treecost += cost(G,e)
    return treecost


#######################################################
#graph_cost returns the total weight of a graph
    
    
    ####prims algo########
#remove edges that make cycles
#make a function find a minimum edge
#return total edge cost of a given graph
