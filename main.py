from algorithms import prims
from functions.graph_operations import graph_cost


text = input('Please provide a graph to run the TSP on ')

vt = input('Please provide a starting vertex ')

T = prims(G, v)

print('Optimal Tree is {T}')

print('')

print('Optimal cost: {graph_cost(T)}')