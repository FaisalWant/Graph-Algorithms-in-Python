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



class AdjacencyMatrixGraph(Graph):
	def __init__(self, numVertices, directed=False):   # change directed =True for getting a directed graph
		super (AdjacencyMatrixGraph,self).__init__(numVertices, directed)
		self.matrix = np.zeros((numVertices, numVertices))


	def add_edge(self, v1, v2, weight=1):
		if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2<0:
			raise ValueError("Vertices %d and %d are out of bounds" %(v1, v2))


		if weight <1:
			raise ValueError("An edge cannot have weight <1")

		self.matrix[v1][v2]= weight


		if self.directed==False:
			self.matrix[v2][v1]=weight



	def get_adjacent_vertices(self, v):
		if v<0 or v>= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v )

		
		adjacent_vertices=[]

		for i in range(self.numVertices):
			if self.matrix[v][i]>0:
				adjacent_vertices.append(i)	

		return adjacent_vertices


	def get_indegree(self, v):
		if v<0 or v>=self.numVertices:
			raise ValueError("cannot access Vertex %d" % v)

		indegree=0
		for i in range(self.numVertices):
			if self.matrix[i][v] >0:
				indegree+= 1

		return indegree


	def get_edge_weight(self, v1, v2):
		return self.matrix[v1][v2]


	def display(self):
		for i in range(self.numVertices):
			for v in self.get_adjacent_vertices(i):
				print(i,"-->", v)


# Topological Sort

def topological_sort(graph):
	queue=Queue()
	indegreeMap={}

	for i in range(graph.numVertices):
		indegreeMap[i]=graph.get_indegree(i)

		if indegreeMap[i]==0:
			queue.put(i)

	sortedList=[]
	while not queue.empty():
		vertex=queue.get()
		sortedList.append(vertex)

		for v in graph.get_adjacent_vertices(vertex):
			indegreeMap[v]=indegreeMap[v]-1

			if indegreeMap[v]==0:
				queue.put(v)


	if len(sortedList) != graph.numVertices:
		raise ValueError("This graph has a  cycle")

	print(sortedList)



g=AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(3,6)
g.add_edge(3,4)
g.add_edge(6,8)


topological_sort(g)