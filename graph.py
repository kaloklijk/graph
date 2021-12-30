"""
This is a library for graph algorithms, networkx and matplotlib is require to use the
 library. Please download networkx using pip install networkx and matplotlib
 using pip install matplotlib
"""
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import defaultdict
class graphOpts:
    def __init__(self):
        self.visited = set()
    def dfs(g, s):
        """
        dfs algorithm starting from s in g
        """

        if s not in g.nodes:
            return
        gg = nx.Graph()
        gg.add_nodes_from(g)
        S = []
        queue = []
        S.append(s)
        queue.append(s)
        while queue:
            s = queue.pop()
            print(s, end = " ")
            for v in g.edges(s): 
                if v[1] not in S:
                    gg.add_edges_from([v])
                    gg.edges[v[0], v[1]]['weight'] = g.edges[v[0], v[1]]['weight']
                    queue.append(v[1]) 
                    S.append(v[1])

        plt.figure("dfs")
        pos = nx.circular_layout(gg)
        labels = nx.get_edge_attributes(gg, 'weight')
        nx.draw(gg, pos, with_labels = True, node_size = 600, node_color = "lightblue", edge_color = "red")
        nx.draw_networkx_edge_labels(gg, pos, edge_labels = labels)

    def bfs(g, s):
        """
        bfs algorithm starting from s in g
        """
        if s not in g.nodes:
            return
        gg = nx.Graph()
        gg.add_nodes_from(g)
        S = []
        queue = []
        S.append(s)
        queue.append(s)
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for v in g.edges(s): 
                if v[1] not in S:
                    gg.add_edges_from([v])
                    gg.edges[v[0], v[1]]['weight'] = g.edges[v[0], v[1]]['weight']
                    queue.append(v[1]) 
                    S.append(v[1])
                    
        plt.figure("bfs")
        pos = nx.circular_layout(gg)
        labels = nx.get_edge_attributes(gg, 'weight')
        nx.draw(gg, pos, with_labels = True, node_size = 600)
        nx.draw_networkx_edge_labels(gg, pos, edge_labels = labels)

    def Dijkstra(g, s):
        visited = set()
        dist = defaultdict() 
        for v in g.nodes:
            dist[v] = 99999999
        dist[s] = 0
        for e in g.edges:
            if e[0] == s:
                pass
                
    def MST(g):
        """
            find the minimum spanning tree of a undirected, weighted graph g
        """
        nodes = g.nodes
        S = []
        while S != nodes:
            pass
        
    
g = nx.generators.random_graphs.fast_gnp_random_graph(10, 0.26)
for (u, v) in g.edges:
    g.edges[u,v]['weight'] = random.randint(1, 11)
plt.figure("graph")
pos = nx.circular_layout(g)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw(g, pos, with_labels = True, node_size = 600, node_color = "lightblue", edge_color = "red")
nx.draw_networkx_edge_labels(g, pos, edge_labels = labels)
graphOpts.dfs(g, 0)
graphOpts.bfs(g, 0)
plt.show()
