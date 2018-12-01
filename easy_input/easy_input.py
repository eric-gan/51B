import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()


# G.add_node_from("1")

G.add_nodes_from([str(i) for i in range(8)])
G.add_edge("1", "2")
G.add_edge("1", "3")
G.add_edge("1", "0")
G.add_edge("2", "3")
G.add_edge("0", "2")
G.add_edge("3", "0")
G.add_edge("4", "5")
G.add_edge("4", "6")
G.add_edge("4", "7")
G.add_edge("5", "6")
G.add_edge("5", "7")
G.add_edge("6", "7")
nx.write_gml(G, "easy_graph.gml")


# print(G.number_of_nodes())
# print(G.number_of_edges())

# for each in list(G.nodes()):
# 	print(each)
