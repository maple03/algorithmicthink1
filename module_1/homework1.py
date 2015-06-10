"""Algorythmic thinking - homework 1"""
EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    """Takes the number of nodes num_nodes 
    and returns a dictionary corresponding 
    to a complete directed graph with the 
    specified number of nodes."""
    graph = {}
    for node in range(num_nodes):
        adjacent_edges = range(num_nodes)
        adjacent_edges.remove(node)
        graph[node] = set(adjacent_edges)
    return graph
        
def compute_in_degrees(digraph):
    """Takes a directed graph digraph 
    (represented as a dictionary) 
    and computes the in-degrees for 
    the nodes in the graph."""
    in_degrees = {}
    for node in digraph.keys():
        in_degrees[node] = 0
    for adjacent_nodes in digraph.values():
        for node in adjacent_nodes:
            in_degrees[node] += 1
    return in_degrees

def in_degree_distribution(digraph):
    """Takes a directed graph digraph 
    (represented as a dictionary) 
    and computes the unnormalized distribution of 
    the in-degrees of the graph."""
    distribution = {}
    in_degrees = compute_in_degrees(digraph)
    for in_degree in in_degrees.values():
        if distribution.has_key(in_degree):
            distribution[in_degree] += 1
        else:
            distribution[in_degree] = 1
    return distribution

#print in_degree_distribution(EX_GRAPH0)
#print in_degree_distribution(EX_GRAPH1)
#print in_degree_distribution(EX_GRAPH2)