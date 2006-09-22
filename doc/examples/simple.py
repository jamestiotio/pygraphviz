#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple example to create a graphviz dot file.

"""
#    Copyright (C) 2006 by 
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Manos Renieris, http://www.cs.brown.edu/~er/
#    Distributed with BSD license.     
#    All rights reserved, see LICENSE for details.

from pygraphviz import *

A=AGraph()

A.add_edge(1,2)
A.add_edge(2,3)
A.add_edge(1,3)

print A.string() # print to screen
A.write("simple.dot") # write to simple.dot