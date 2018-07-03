#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:49:37 2018

@author: lizhang
"""
#########################################
# Load libraries
from sklearn.preprocessing import MultiLabelBinarizer
import pickle
from scipy import sparse
import scipy.sparse as sp
import numpy as np
import scipy.io as scio
import networkx as nx
import random

"*********** produce the labels **********"
with open("blogCatalog3-groups.txt","r") as fin:
    firstline=fin.readline().strip().split()
    label=[]
    for line in fin:
        line=line.strip().split(':')
        label.append(line[1].split())
    one_hot = MultiLabelBinarizer()
    new_label=one_hot.fit_transform(label)
    pickle.dump (new_label[0:1000],open("ind.blog.y","wb"))
    pickle.dump (new_label[9312:10312],open("ind.blog.ty","wb"))
    pickle.dump (new_label[0:9312],open("ind.blog.ally","wb"))

"********** produce the features **********"
a = []
a0 = scio.loadmat('blogcatalog.mat') 
a1 = a0['network']
pickle.dump (a1[0:1000],open("ind.blog.x","wb"))
pickle.dump (a1[9312:10312],open("ind.blog.tx","wb"))
pickle.dump (a1[0:9312],open("ind.blog.allx","wb"))

"********** produce the graph **********"
a2 = a1.tolil(copy=False)
pickle.dump (a2,open("ind.blog.graph","wb"))

"********** produce the index **********"
nums = [x for x in range(9312,10312)]
random.shuffle(nums)
index0 = list(map(int,nums))
np.savetxt("index.txt",index0)
a3 = np.loadtxt("index.txt").astype(int)
np.savetxt("newindex.txt", a3,fmt="%d")
