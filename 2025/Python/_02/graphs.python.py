import networkx

# Create the graph
Graph = networkx.Graph()

# Building the graph visual, determine via a program:
map = [ ('A', 'D'), ('D', 'B'), ('D', 'G'), ('D', 'H'), ('G', 'E'), ('B', 'F'), ('E', 'F'), ('E', 'I') ]
Graph.add_edges_from(map)

# The shortest path between A and I
shortest_path = networkx.shortest_path(Graph, source='A', target='I')
print(f"The shortest path between A and I - {shortest_path}")

# # The node with the most edges
degrees = dict(Graph.degree())
max = max(degrees, key=degrees.get)
print(f"The node with the most edges - {max}")

# All isolated nodes
nodes = set('ABCDEFGHI')
Graph.add_nodes_from(nodes)
isolates = list(networkx.isolates(Graph))
print(f"All isolated nodes - {isolates}")