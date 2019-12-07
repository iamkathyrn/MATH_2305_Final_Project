

# prims goes here
def prims(textfile):
    G = get_graph(textfile)
    T = initialize_tree(G, v)
    
    while T[0] != G[0]:
        e = min_cost_edge(G, T)
        # add e and its vertices to T
