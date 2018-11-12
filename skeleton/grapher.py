import networkx as nx
import matplotlib.pyplot as plt
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

INSIDE = 3 # change me
CHILDREN = 4 # change me

# second is number of nodes in second level
# children is number of nodes per second layer node
# generates a graph where second layer is completely connected
def gen(inside, children):
	# generate completely connected graph
	K = nx.complete_graph(inside)
	# change all nodes to strings
	mapping = {}
	for x in range(inside):
		mapping[x] = str(x)
	K = nx.relabel_nodes(K, mapping)
	# add each layer three node sequentially
	heighest = inside
	for i in range(inside):
		for j in range(children):
			node_name = str(heighest)
			K.add_node(node_name)
			base = str(i)
			K.add_edge(base, node_name)
			heighest += 1
	return K

G = gen(INSIDE, CHILDREN)
for i in range(INSIDE, INSIDE * (CHILDREN + 1) - 1):
	u = str(i)
	v = str(i + 1)
	G.add_edge(u, v)
G.add_edge(str(INSIDE * (CHILDREN + 1) - 1), str(INSIDE))



# plot graph
nx.draw_networkx(G)
plt.show()

nx.write_gml(G, "./folder/graph.gml")