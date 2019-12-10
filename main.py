from algorithms.prims_algorithm import prims
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

#MST - minimum spanning tree

input_graph = get_graph('G1.txt') 
start_node = int(input(f'Choose a starting node, {input_graph[0]}: ')) 
print('')


prims_MST = prims(input_graph, start_node)

total_tree_weight = total_tree_weight(input_graph, prims_MST)

vertices, edges = prims_MST

###############################################################################
#######################     PRINT RESULTS    ##################################
      
print('')
print('Prim''s algorithm - MST - "minimum spanning tree"')
print('')
print('')
print(f'MST NODES : {vertices}')
print(f'MST EDGES : {edges}')
print('')
print(f'MST WEIGHT (cost): {total_tree_weight}')