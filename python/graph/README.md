# Code Challenge 35 - Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
building a graph class that includes the following methods:

    add_node
    add_edge
    get_nodes
    get_edges
    get_neighbors


## API
+ add node
    +    Arguments: value
    +    Returns: The added node
    +    Add a node to the graph
+ add edge
    + Arguments: 2 nodes to be connected by the edge,  weight (optional)
    + Returns: nothing
    + Adds a new edge between two nodes in the graph
    + If specified, assign a weight to the edge
    + Both nodes should already be in the Graph
+ get nodes
    + Arguments: none
    + Returns all of the nodes in the graph as a collection (set, list, or similar)
+ get neighbors
    + Arguments: node
    + Returns a collection of edges connected to the given node
    + Include the weight of the connection in the returned collection
+ size
    + Arguments: none
    + Returns the total number of nodes in the graph
## Check list

https://github.com/mohammadsilwadi/data-structures-and-algorithms/pull/43

# Code Challenge 36 | breadth-first traversal
- Implement a breadth-first traversal on a graph.


## Whiteboard Process
![](cc36.jpg)

## Approach & Efficiency
- time ==> O(n)
- space ==> O(n)

## Solution
```
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

```
https://github.com/jariryyousef/data-structures-and-algorithms/pull/45


# Code Challenge 37 | Graph business trip
- Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?


## Whiteboard Process
![](CodeChallange37.jpg)

## Approach & Efficiency
- time ==> O(n^2)
- space ==> O(1)

## Solution
```
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
```
https://github.com/jariryyousef/data-structures-and-algorithms/pull/46
