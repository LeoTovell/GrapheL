from Vertex import Vertex

class Graph:
	def __init__(self, name):
		self.name = name
		self.vertex_list = []

	def get_vertices(self):
		return self.vertex_list

	def create_default_values(self):
		# Create defaults
		default_vertices = ["A", "B", "C", "1", "2", "3"]
		default_edges = [["A", "B", 10],
						["B", "C", 8],
						["C", "1", 2],
						["1", "2", 4],
						["2", "3", 7],
						["3", "A", 4],
						["B", "2", 8]]
		for vertex in default_vertices:
			self.create_vertex(vertex)

		for edge in default_edges:
			self.add_named_edge(edge[0], edge[1], edge[2])


	def compile_adjacency_list(self):
		# Setup list
		adjacency_list = []
		for vertex in self.vertex_list:
			content = [vertex]
			for neighbour in vertex.get_neighbours(self.vertex_list):
				content.append([neighbour, self.get_edge(vertex, neighbour).get_weight()])
			adjacency_list.append(content)
		return adjacency_list

	def compile_adjacency_list_debug(self):
		# Setup list
		adjacency_list = []
		for vertex in self.vertex_list:
			content = [vertex.get_name()]
			for neighbour in vertex.get_neighbours(self.vertex_list):
				content.append([neighbour.get_name(), self.get_edge(vertex, neighbour).get_weight()])
			adjacency_list.append(content)
		return adjacency_list


	def compile_adjacency_matrix(self):
		# Unlikely to be used
		pass

	def find_vertex(self, name):
	# Search through all vertices and return either null or the vertex.
		for vertex in self.vertex_list:
			if vertex.get_name() == name:
				return vertex
		return None

	def create_vertex(self, name):
		# create a new vertex with supplied name and create the position automatically.
		existing_vertex = None
		for vertex in self.vertex_list:
			if vertex.get_name() == name:
				existing_vertex = vertex
		if existing_vertex == None:
			vertex = Vertex(name)
			self.vertex_list.append(vertex)
			return True
		else:
			print(f"Vertex with the name: {name}, already exists, process aborted")
			return false

	def create_pos_vertex(self, x, y):
		# create a new vertex with supplied position and create the name automatically.

		pass

	def remove_vertex(self, vertex):
		# Remove the edges attached to and from the vertex and then delete the vertex from the vertex list
		edges_to_delete = []
		for vertex in self.vertex_list:
			for edge in vertex.get_edges():
				if edge.get_start() == vertex:
					edges_to_delete.append(edge)
		for edge in edges_to_delete:
			self.remove_edge(edge.get_start(), edge.get_end())
		self.vertex_list.remove(vertex)


	def add_edge(self, source, destination, weight):
		# Add the edge from source to destination
		source.add_edge(destination, weight, self.vertex_list)

	def add_named_edge(self, source, destination, weight):
		# Add the edge from string to string (use find_vertex)
		source_vertex = None
		destination_vertex = None
		for vertex in self.vertex_list:
			if vertex.get_name() == source:
				source_vertex = vertex
			elif vertex.get_name() == destination:
				destination_vertex = vertex

		if source_vertex != None and destination_vertex != None:
			source_vertex.add_edge(destination_vertex, weight, self.vertex_list)
		else:
			print("Error, source/destination vertex not found")

	def remove_edge(self, source, destination):
		# Params are vertexs, not strings
		source.remove_edge(destination)
		destination.remove_edge(source)

	def get_edge(self, source, destination):
		# Loop through all vertices and get the edge: source -> edge OR edge -> source
		for vertex in self.vertex_list:
			for edge in vertex.get_edges():
				if (edge.get_start() == source and edge.get_end() == destination) or (edge.get_start() == destination and edge.get_end() == source):
					return edge
		return None

	# DO NOT HANDLE GRAPHICS ON SERVER (DONE WITH WEBGL ON CLIENT SIDE)