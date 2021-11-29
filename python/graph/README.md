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
https://github.com/jariryyousef/data-structures-and-algorithms/pull/46
