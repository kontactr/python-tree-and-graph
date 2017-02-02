# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from anytree import Node, RenderTree
import pydot

def gp(node1,node2):	
	a , b = str(node1) , str(node2)
	print (a,b)


graph = pydot.Dot(graph_type='graph')

gf_f = Node("gf_f")
gm_f = Node("gm_f")
gf_m = Node("gf_m")
gm_m = Node("gm_m")
f = Node("f",parent=gf_f)
f = Node("f",parent=gf_m)
m = Node("m",parent=gm_f)
m = Node("m",parent=gm_m)
ch1 = Node("ch1",parent=f)
ch1 = Node("ch1",parent=m)
ch2 = Node("ch2",parent=f)
ch2 = Node("ch2",parent=m)

edge = pydot.Edge("gf_f", "f")
graph.add_edge(edge)
edge = pydot.Edge("gm_f", "f")
graph.add_edge(edge)
edge = pydot.Edge("gf_m", "m")
graph.add_edge(edge)
edge = pydot.Edge("gm_m", "m")
graph.add_edge(edge)
edge = pydot.Edge("f", "ch1")
graph.add_edge(edge)
edge = pydot.Edge("f", "ch2")
graph.add_edge(edge)
edge = pydot.Edge("m", "ch1")
graph.add_edge(edge)
edge = pydot.Edge("m", "ch2")
graph.add_edge(edge)


graph.write_png("family.png")

gp(ch1,ch2)

#for node present in string line root/child-3
#print (str(d)[6:len(str(d))-2])
