from Edge import Edge

class Vertex:
	def __init__(self, name):
		self.name = name
		self.edge_list = []
		# self.x = x
		# self.y = y

	def add_edge(self, destination, weight, all_vertices):
		if destination == self:
			print("Cannot create edge to self!")
			return None
		for vertex in all_vertices:
			for edge in vertex.get_edges():
				if (edge.get_start() == self and edge.get_end() == destination) or (edge.get_start() == destination and edge.get_end() == self):
					print("Edge already exists.")
					return None
		edge = Edge(self, destination, weight)
		self.edge_list.append(edge)
		return edge


	def remove_edge(self, destination):
		edges_to_remove = []
		for edge in self.get_edges():
			if edge.get_end() == destination:
				edges_to_remove.append(edge)
		for edge in edges_to_remove:
			self.edge_list.remove(edge)

	def get_neighbours(self, all_vertices):
		neighbours = []
		for edge in self.get_edges():
			neighbours.append(edge.get_end())
		for vertex in all_vertices:
			for edge in vertex.get_edges():
				if edge.get_end() == self:
					neighbours.append(edge.get_start())
		return neighbours

	def has_coords(self):
		return (y != None and x != None)

	def get_name(self):
		return self.name

	def get_edges(self):
		return self.edge_list