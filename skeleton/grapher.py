import networkx as nx
G = nx.Graph()


# G.add_node("1")

# G.add_nodes_from(["2", "3"])

# G.add_edge("1","2")

# G.add_edge("2", "3")

# print(G.number_of_nodes())
# print(G.number_of_edges())

# for each in list(G.nodes()):
# 	print(each)








# for each in list(K.nodes()):
# 	print("complete: " + str(each))




def gen(second, children):
	K = nx.complete_graph(second)
	mapping = {}
	for x in range(second):
		mapping[x] = str(x)
	K = nx.relabel_nodes(K, mapping)
	heighest = second
	for i in range(second):
		for j in range(children):
			node_name = str(heighest)
			K.add_node(node_name)
			base = str(i)
			print(base)
			print(node_name)
			K.add_edge(base, node_name)
			heighest += 1
	return K

G = gen(3, 2)

print(G.edges())

nx.write_gml(G, "./folder/graph.gml")