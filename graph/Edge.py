class Edge:
	def __init__(self, source, destination, weight):
		self.source = source
		self.destination = destination
		self.weight = weight

	def get_midpoint(self):
		return [(source.get_x() + destination.get_x())/2, (source.get_y() + destination.get_y()) /2]

	def get_weight(self):
		return self.weight

	def to_string(self):
		return "Start: " + self.source.get_name() + ", End: " + self.destination.get_name() + ", Weight: " + str(self.get_weight())

	def get_start(self):
		return self.source

	def get_end(self):
		return self.destination