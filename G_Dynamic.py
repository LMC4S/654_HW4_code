#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: rahrah

Python 3.6

Glauber dynamics on hardcore configurations.
"""

import networkx as nx
import numpy as np
import random


L = 5
G=nx.grid_2d_graph(L,L)


# Do the neighbors of a node have a particle?
def test_neighbors(node):
    if any([1 == particles[node] for node in G.neighbors(node) ]):
        return True
    else:
        return False
 

particles = dict( (node, 0) for node in G.nodes()) # dicitonary to store particle locations
particles[(0,0)] = 1 # put a particle at node (0,0)

def run_chain(x):
    for i in range(T):
        n = random.choice(list(G.nodes()))
        if test_neighbors(n) == False:
            x[n] = random.choice([0,1])
    return x
T=1000
run_chain(particles)    
nx.draw(G, with_labels=True, pos=nx.layout.spectral_layout(G), font_size=7, node_color=[particles[node] for node in G.nodes()])
    
    