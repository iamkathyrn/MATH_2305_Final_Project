from functions.graph_operations import min_cost_incident_edge, incident_edges, init_tree


def prims(input_graph, start_node):
    tree = init_tree(start_node)
    
    
    all_known_paths = incident_edges(input_graph, tree)          

    #while ((length (tree nodes)) != (length of the (graph nodes)))
    while (len(tree[0]) != len(input_graph[0])): 
        #loops to check all possible paths in tree p-(path)
        for p in all_known_paths:
            for node_1 in tree[0]:
                for node_2 in tree[0]:         
                    #comparing path values and append edge of smallest path found
                    if (p == min_cost_incident_edge(input_graph, tree)) and ( str(p) != '(' + str (node_1) + ', ' + str(node_2) + ')' ): 
                        tree[1].append(p)
                        
            #Loops through all nodes in tree e-(edge)
            for e in tree[1]:
                #Loops and checks all nodes in edges
                for node in e:
                    #append node not in tree
                    if (node not in tree[0]):
                        tree[0].append(node)
                        all_known_paths = incident_edges(input_graph, tree)          
            
    return tree

