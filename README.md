# MATH_2305_Final_Project
# Minimum Spanning Tree using Prim's algorithm in Python

### reading_writing_function.py

  Creates a dictionary of tuples from our data (G1.txt) to manipulate.
  
### test.py
  Used to build and test functions and later move them into their correct places once we knew they worked.
  
### main.py
  
  Our main where all functions are called and results are formatted and displayed
  
### graph_operations.py

  def incident_edges (input_graph, tree):
  
    #gives all adjacent NODES to current NODES currently in our graph
    
  def cost (input_graph, edge):
  
    #return weight (cost) of edges in graph
    
  def initialize_tree (start_node):
  
    #build and return our tree to begin adding nodes and edges
    
  def min_cost_incident_edge(input_graph, tree):
  
    #return minimum edge through comparision of edges
    
  def total_tree_weight(input_graph, prims_MST):
  
    #return total weight of tree (cost)
    
### prims_algorithm.py

  adds nodes and edges to tree - non-circular
