import numpy as np
from queue import Queue
import abc
class Graph(abc.ABC):
	def __init__(self, numVertices, directed=False):
		self.numVertices=numVertices
		self.directed=directed


	@abc.abstractmethod
	def add_edge(self, v1, v2, weight):
		pass


	@abc.abstractmethod
	def get_adjacent_vertices(self, v):
		pass


	@abc.abstractmethod
	def get_indegree(self, v):
		pass


	@abc.abstractmethod
	def display(self):
		pass




class Node:
	def __init__(self, vertexId):
		self.vertexId= vertexId
		self.adjacency_set= set()


	def add_edge(self, v):
		if self.vertexId==v:
			raise ValueError("The vertext %d cannot be adjacent to itself" % v)

		self.adjacency_set.add(v)

	def get_adjacent_vertices(self):
		return sorted(self.adjacency_set)




class AdjacencySetGraph(Graph):
	def __init__(self, numVertices, directed=False):
		super(AdjacencySetGraph, self).__init__(numVertices, directed)
		self.vertex_list =[]
		for i in range(numVertices):
			self.vertex_list.append(Node(i))


	def add_edge(self, v1, v2, weight=1):
		if v1>= self.numVertices or v2>= self.numVertices or v1<0 or v2<0:
			raise ValueError("Vertices %d and %d are out of bounds" %(v1,v2))


		if weight !=1:  #will be accepting only those graphs with edge weight equal to one
			raise ValueError("An adjacenc set cannot represent edge weights >1")

		self.vertex_list[v1].add_edge(v2)
		if self.directed==False:
			self.vertex_list[v2].add_edge(v1)

	
	def get_adjacent_vertices(self, v):
		if v<0 or v>= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)


		return self.vertex_list[v].get_adjacent_vertices()


	def get_indegree(self, v):
		if v<0 or v>=self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)

		indegree=0
		for i in range(self.numVertices):
			if v in self.get_adjacent_vertices(i):
				indegree= indegree+1


		return indegree



	def get_edge_weight(self, v1,v2):
		return 1


	def display(self):
		for i in range(self.numVertices):
			for v in self.get_adjacent_vertices(i):
				print(i, "--->",v)



def build_distance_table(graph, source):
	#seting data table as disctionary

	distance_table={}
	for i in range(graph.numVertices):
	 	distance_table[i]=(None, None)


	distance_table[source]=(0, source)

	queue=Queue()
	queue.put(source)
	while not queue.empty():
		current_vertex =queue.get()

		current_distance= distance_table[current_vertex][0]
		for neighbor in graph.get_adjacent_vertices(current_vertex):
			if distance_table[neighbor][0] is None:
				distance_table[neighbor]= (1+current_distance, current_vertex)

				if len(graph.get_adjacent_vertices(neighbor))>0:
					queue.put(neighbor)

	return distance_table




def shortest_path(graph, source, destination):
	distance_table= build_distance_table(graph, source)
	path=[destination]
	previous_vertex= distance_table[destination][1]
	while previous_vertex is not None and previous_vertex is not source:
		path= [previous_vertex]+path
		previous_vertex= distance_table[previous_vertex][1]

	if previous_vertex is None:
		print("There is no path from %d to %d" %(source, destination))

	else:
		path=[source] + path
		print("Shortest path is ", path)


g=AdjacencySetGraph(8, directed=False)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(3,6)
g.add_edge(6,7)
g.add_edge(0,7)


shortest_path(g, 0,5)
shortest_path(g, 0,6)
shortest_path(g, 7,4)