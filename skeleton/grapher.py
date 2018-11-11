import networkx as nx
G = nx.Graph()


G.add_node("1")

G.add_nodes_from(["2", "3"])

G.add_edge("1","2")

G.add_edge("2", "3")

print(G.number_of_nodes())
print(G.number_of_edges())

for each in list(G.nodes()):
	print(each)

nx.write_gml(G, "./folder/graph.gml")