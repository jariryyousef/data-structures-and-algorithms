from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.
    
    """
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()
        
    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.
		
		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()


class Edge:
    """ 
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    
  """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self._adjacency_list = {}

    def add_node(self, value):
        """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
        # new node
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self._adjacency_list.get(vertex, [])



#######################################Code Challange 36############################################## 
    def breadth_first_search(self, start_vertex):
        queue = Queue()
        visited = set()
        nodes = []
        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()

            neighbors = self.get_neighbors(current_vertex)
            nodes.append(current_vertex.value)
            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return nodes

  
####################################### Code Challange 37 ############################################## 

    def business_trip(self,cities):
            if len(cities) == 0:
                return False,'$0'
            if self._adjacency_list[cities[0]] == []:
                return False,'$0'

            count = 0
            path = False

            for i in range(len(cities)-1):
                neighbors = self._adjacency_list[cities[i]]

                for j in neighbors:

                    if cities[i+1].value == j.vertex.value:
                        count += j.weight
                        path = True
                        break
                    
                    else:
                        count += 0
                        path = False
            
            if not path:
                return False,'$0'
            
            return True,'$'+ str(count)

####################################### Code Challange 38 ############################################## 


    def graph_depth_first(self, vertex=None):
        if not vertex:
            return[]
        visited = set()
        nodes = []

        def rec_fun(node):
            neighbors = self.get_neighbors(node)
            for i in neighbors:
                node_v = i.vertex
                if node_v in visited:
                    continue
                else:
                    nodes.append(node_v)
                    visited.add(node_v)
                    rec_fun(node_v)

        nodes.append(vertex)
        rec_fun(vertex)
        return nodes