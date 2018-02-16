#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rahrah

Python 3.6


MCMC for uniform distribution as stationary distribution
"""

import networkx as nx
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

G=nx.powerlaw_cluster_graph(20, 7, 0.3, seed=654) 
G=nx.Graph(G) 
G.remove_edges_from(G.selfloop_edges()) 


T = 100000
def accept(x, y):
    accept_prob = min(1, len(list(G.neighbors(x))) / len(list(G.neighbors(y))))
    # acceptance probability: min(1, deg(x) / deg(y) )
    return 1 == np.random.binomial(1, accept_prob)
    
def simple_walk_from(x):
    candidate = random.choice(list(G.neighbors(x))) 
    # sample uniformly among neighbors of x
    if accept(x, candidate):
        return candidate
    else:
        return x
    
def run_chain_starting_from(x_zero):
    visited_nodes = []
    current_node = x_zero
    for i in range(T):
        visited_nodes.append(current_node)
        current_node = simple_walk_from(current_node)
    return visited_nodes
        
# Run the Markov chain   
from collections import Counter
counts = Counter(run_chain_starting_from(18))

# Draw histogram
def counts_of_time_node_was_visited(node):
    return counts[node]

def simple_walk_stationary_distribution(node):
    return G.degree(node)/float(2*len(G.edges()))
                                
    
data = dict( (
                node, (
                    counts_of_time_node_was_visited(node), # first column
                    simple_walk_stationary_distribution(node)) # second column
             )
            for node in G.nodes())
df = pd.DataFrame(data).transpose()
df = df[0]
df.plot(kind="bar")

