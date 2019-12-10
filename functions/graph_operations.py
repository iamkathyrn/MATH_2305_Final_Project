def incident_edges (input_graph, tree):
    #gives all adjacent NODES to current NODES currently in our graph
    tree_NODES = []
    
    for edge in input_graph[1]:
        for node_1 in tree[0]:
            for node_2 in tree[0]:
                if (node_1 in edge) and (edge not in tree[1]) and (edge not in tree_NODES):
                    tree_NODES.append(edge)
        
    for edge in tree_NODES:
        for node_1 in tree[0]:
            for node_2 in tree[0]:
                #if (2 of the same nodes in tree) - delete - removes circular graphs)
                #if  ( ( '('+str(node_1) + ', ' + str(node_2)+')' ) == str(edge)   ):
                if  ( ( '('+str(node_1) + ', ' + str(node_2)+')' ) == str(edge)   ):
                    del tree_NODES[ tree_NODES.index(edge) ]

    return tree_NODES

def cost (input_graph, edge):
    #return weight (cost) of edges in graph
    return input_graph[1][edge]

def initialize_tree (start_node):
    #build and return our tree to begin adding nodes and edges to
    return (([start_node],[]))

###############################################################################
def min_cost_incident_edge(input_graph, tree):
    #return minimum edge through comparision of edges
    new_nodes = incident_edges(input_graph, tree)
    minimum_edge = new_nodes[0]

    for j in new_nodes:
        if ((input_graph[1][minimum_edge] >= input_graph[1][j])):
            minimum_edge = j

    return minimum_edge 
    
def total_tree_weight(input_graph, prims_MST):
    #return total weight of tree (cost)
    total_tree_weight = 0
 
    #looping thorugh all nodes in created MST
    for e in range(0, len( prims_MST[1] ) ):
        total_tree_weight = total_tree_weight + cost(input_graph, prims_MST[1][e] )
        
    return total_tree_weight
