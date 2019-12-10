from functions.graph_operations import min_cost_incident_edge, incident_edges, initialize_tree


def prims(input_graph, start_node):
    Tree = initialize_tree(start_node)
    avalible_paths = incident_edges(input_graph, Tree)          
    path_to_take = min_cost_incident_edge(input_graph, Tree)

    while (len(Tree[0]) != len(input_graph[0])): #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 
    
        for path in avalible_paths:  #Checks all avalible paths
            for vertex_a in Tree[0]:
                for vertex_b in Tree[0]:                        
                    if ( path == min_cost_incident_edge(input_graph, Tree)) and ( str(path) != '(' + str (vertex_a) + ', ' + str(vertex_b) + ')' ):     #Only allows for the smallest path to be taken and adds that path/edge to our working tree  
                        Tree[1].append(path)
        
            for edge in Tree[1]:   #Runs through all edges in our working tree 
                for vertice in edge: #And vertices in those edges
                    if vertice not in Tree[0]:  #And adds the vertex if it isnt in out working tree. 
                        Tree[0].append(vertice)
                        avalible_paths = incident_edges(input_graph, Tree)          
                        path_to_take = min_cost_incident_edge(input_graph, Tree)  
            
    return Tree

