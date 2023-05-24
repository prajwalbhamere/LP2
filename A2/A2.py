# A* Search Algorithm
#
# let openList equal empty list of nodes
# let closedList equal empty list of nodes
# put startNode on the openList (leave it's f at zero)
# while openList is not empty
#     let currentNode equal the node with the least f value
#     remove currentNode from the openList
#     add currentNode to the closedList
#     if currentNode is the goal
#         You've found the exit!
#     let children of the currentNode equal the adjacent nodes
#     for each child in the children
#         if child is in the closedList
#             continue to beginning of for loop
#         child.g = currentNode.g + distance b/w child and current
#         child.h = distance from child to end
#         child.f = child.g + child.h
#         if child.position is in the openList's nodes positions
#             if child.g is higher than the openList node's g
#                 continue to beginning of for loop
#         add the child to the openList

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with distances from the current node to the goal node
    def h(self, n):
        H = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjac_lis = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'D': [('G', 1)],
    'E': [('D', 6)]
}

graph = Graph(adjac_lis)
graph.a_star_algorithm('A', 'G')


# Explanation:
# This code implements the A* algorithm for finding the shortest path between two nodes in a graph. 
# The graph is represented using an adjacency list.

# The `Graph` class has an `__init__` method that takes an `adjacency_list` as input. The `adjacency_list` 
# is a dictionary where the keys represent nodes, and the values are lists of tuples. Each tuple contains a 
# neighboring node and the weight of the edge connecting them.

# The `get_neighbors` method returns the list of neighbors for a given node.

# The `h` method is a heuristic function that estimates the cost from a given node to the goal node. 
# It assigns a heuristic value for each node based on the distances provided in the `H` dictionary.

# The `a_star_algorithm` method performs the A* search algorithm to find the shortest path from `start_node` 
# to `stop_node`. It uses open_list and closed_list sets to keep track of visited nodes. The `g` dictionary 
# stores the current distances from the `start_node` to all other nodes. The `parents` dictionary keeps track 
# of the parent node for each visited node.

# The algorithm starts by adding the `start_node` to the open_list with a distance of 0. It iterates until 
# the open_list is empty. In each iteration, it selects the node with the lowest evaluation function value (`f()`) 
# based on the sum of the distance from the `start_node` (`g` value) and the heuristic value (`h` value). 
# If there is no node to select, it means that a path does not exist, and the algorithm returns `None`.

# If the current node is the `stop_node`, the algorithm reconstructs the path from the `stop_node` to the 
# `start_node` using the `parents` dictionary. It appends each node to the `reconst_path` list, starting from 
# the `stop_node` and following the parent links until reaching the `start_node`. The `reconst_path` list is then 
# reversed to obtain the correct order of the path from the `start_node` to the `stop_node`. The path is printed 
# and returned.

# For each neighbor of the current node, the algorithm checks if the neighbor is already in the open_list or 
# closed_list. If not, it adds the neighbor to the open_list, updates its parent and distance values, and 
# calculates the `g` value as the sum of the current node's `g` value and the weight of the edge between the nodes. 
# If the neighbor is already in the open_list or closed_list, the algorithm checks if reaching it through the current 
# node results in a shorter distance. If it does, the neighbor's parent and `g` values are updated accordingly.

# Finally, the current node is removed from the open_list and added to the closed_list, as all of its neighbors have been inspected.

# In the main block, an adjacency list is defined representing a graph. An instance of the `Graph` class is 
# created with the adjacency list, and the A* algorithm is called to find the shortest path from node 'A' to node 'G'.

# The output of the program will be:
# ```
# Path found: ['A', 'E', 'D', 'G']
# ```

# This indicates that the shortest path from node 'A' to node 'G' is 'A' -> 'E' -> 'D' -> 'G', with a total weight of 10.