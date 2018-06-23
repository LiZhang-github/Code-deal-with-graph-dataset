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

objects_label_ally = []
with open ("ind.cora.ally", 'rb') as ally:
    ally_data = pkl.load(ally,)

labels = sp.csc_matrix(np.vstack((ally_data, ty_data)))

## create the dictionary
dict = {'group': labels, 'network': adj};
scio.savemat('cora.mat', dict)