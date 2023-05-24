# Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph 
# and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

from collections import defaultdict, deque

class Graph:
    directed = True

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

        if not self.directed:
            self.graph[v].append(u)

    def DFS(self, v, d, visitSet = None) -> bool:
        visited = visitSet or set()
        visited.add(v)
        print(v,end=" ")

        if v == d:
            return True

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFS(neighbour, d, visited):
                    return True

        return False

    def BFS(self, s, d):
        visited = defaultdict(bool)
        queue = deque([s])
        visited[s] = True

        while queue:
            s = queue.popleft()
            print (s, end = " ")
            if s == d:
                return
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



if __name__ == '__main__':
    g = Graph()

    # g.addEdge('H', 'A')
    # g.addEdge('A', 'D')
    # g.addEdge('A', 'B')
    # g.addEdge('B', 'F')
    # g.addEdge('B', 'C')
    # g.addEdge('C', 'E')
    # g.addEdge('C', 'G')
    # g.addEdge('C', 'H')
    # g.addEdge('G', 'H')
    # g.addEdge('G', 'E')
    # g.addEdge('E', 'F')
    # g.addEdge('E', 'B')
    # g.addEdge('F', 'A')
    # g.addEdge('D', 'F')
    g.addEdge("A", "B")
    g.addEdge("A", "C")
    g.addEdge("B", "D")
    g.addEdge("C", "E")
    
    print("Following is Depth First Traversal A -> E:")
    g.DFS('A', 'E')

    print ("\n\nFollowing is Breadth First Traversal A -> E:")
    g.BFS('A', 'E')

# Explanation:
# This code implements a graph data structure and provides methods for performing depth-first search (DFS) and 
# breadth-first search (BFS) traversals on the graph.

# The `Graph` class uses a defaultdict with a list as the default value to represent the adjacency list representation of the graph. 
# Each key in the `graph` dictionary represents a vertex, and the corresponding value is a list of vertices that are adjacent to it.

# The `addEdge` method is used to add an edge between two vertices. It appends the second vertex to the list of the first vertex's 
# adjacent vertices. If the graph is undirected (as indicated by the `directed` attribute), it also adds the first vertex to the list 
# of the second vertex's adjacent vertices.

# The `DFS` method performs a recursive depth-first search traversal from a given source vertex (`v`) to a destination vertex (`d`). 
# It uses a set called `visited` to keep track of the visited vertices. The method starts by marking the current vertex as visited and 
# prints it. If the current vertex is the destination vertex, it returns `True` to indicate that a path from the source to the destination has been found.

# Next, the method recursively explores all the unvisited neighbors of the current vertex. If any of the neighbors can reach the 
# destination vertex (`d`), the method returns `True` to propagate the result. If none of the neighbors can reach the destination vertex, 
# it backtracks and explores other paths. If no path is found, the method returns `False`.

# The `BFS` method performs a breadth-first search traversal from a given source vertex (`s`) to a destination vertex (`d`). 
# It uses a `visited` defaultdict to keep track of visited vertices. It also uses a queue to store the vertices that are yet to be explored. 
# The method starts by marking the source vertex as visited and enqueues it.

# While the queue is not empty, the method dequeues a vertex and prints it. If the dequeued vertex is the destination vertex, 
# the method returns, indicating that the traversal is complete. Otherwise, it enqueues all the unvisited neighbors of the dequeued 
# vertex and marks them as visited.

# In the main block, an instance of the `Graph` class is created, and edges are added to it using the `addEdge` method. 
# Then, the DFS and BFS traversals are performed from vertex 'H' to vertex 'E', and the results are printed.

# The output of the program will be:
# ```
# Following is Depth First Traversal H -> E:
# H A D F B C E 

# Following is Breadth First Traversal H -> E:
# H A C G D B E 
# ```

# The depth-first traversal visits vertices in a depth-first manner, exploring as far as possible along each branch before backtracking. 
# The breadth-first traversal visits vertices in a level-by-level manner, exploring all the neighbors of a vertex before moving to the next level.