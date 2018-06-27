#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 13:41:54 2018

@author: li
"""

import pickle as pkl
import scipy.sparse as sp
import numpy as np
import scipy.io as scio
import networkx as nx

## load the data from GCN
objects_graph = []
with open ("ind.cora.graph", 'rb') as g:
    g_data = pkl.load(g, encoding='latin1')
    adj = nx.adjacency_matrix(nx.from_dict_of_lists(g_data)) 

objects_label_ty = []
with open ("ind.cora.ty", 'rb') as ty:
    ty_data = pkl.load(ty)
""" Deal with some isolated node in the graph
    and this is refered to https://github.com/tkipf/gcn
# Fix citeseer dataset (there are some isolated nodes in the graph)
# Find isolated nodes, add them as zero-vecs into the right position
with open ("ind.citeseer.y", 'rb') as y:  
    y = pkl.load(y)  
    
    def parse_index_file(filename):
        index = []
        for line in open(filename):
            index.append(int(line.strip()))
        return index
    
    test_idx_reorder = parse_index_file("ind.citeseer.test.index")
    test_idx_range = np.sort(test_idx_reorder)
    test_idx_range_full = range(min(test_idx_reorder), max(test_idx_reorder)+1)
    ty_extended = np.zeros((len(test_idx_range_full), y.shape[1]))
    ty_extended[test_idx_range-min(test_idx_range),:]=ty_data
    ty_data = ty_extended
"""    
objects_label_ally = []
with open ("ind.cora.ally", 'rb') as ally:
    ally_data = pkl.load(ally,)

labels = sp.csc_matrix(np.vstack((ally_data, ty_data)))

## create the dictionary
dict = {'group': labels, 'network': adj};
scio.savemat('cora.mat', dict)
