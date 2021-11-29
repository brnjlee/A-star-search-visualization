from queue import PriorityQueue
from math import sqrt
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        # edges is a 2d array of weights from node i to node j
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]

        # nodeCoords is an array containing the longitudal and latitudal coordinates
        self.nodeCoords = [(0,0) for i in range(num_of_vertices)]

        # visited is an array containing the nodes assessed throughout the pathfinding process
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def add_node_coord(self, u, coord):
        self.nodeCoords[u] = coord
    
    def euclidean(self, p, q):
        return sqrt((q[0]-p[0])^2 + (q[1]-p[1])^2)

    def a_star(self, start_vertex, end_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, 0, start_vertex, -1))

        while not pq.empty():
            (f, dist, current_vertex, parent) = pq.get()
            self.visited.append([current_vertex, parent])
            if current_vertex == end_vertex:
                break

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    euclidean_to_dest = self.euclidean(self.nodeCoords[current_vertex], self.nodeCoords[end_vertex])
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost + euclidean_to_dest, new_cost, neighbor, current_vertex))
                            D[neighbor] = new_cost
        return self.visited


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

g.add_node_coord(0, (0,1))
g.add_node_coord(1, (1,2))
g.add_node_coord(2, (2,2))
g.add_node_coord(3, (3,2))
g.add_node_coord(4, (2,1))
g.add_node_coord(5, (4,1))
g.add_node_coord(6, (1,0))
g.add_node_coord(7, (2,0))
g.add_node_coord(8, (3,0))

# print(g.edges)
path = g.a_star(0,5)

print("To", path[-1][0], "from", path[-1][1])
parent = path[-1][1]
for i in range(len(path)-2, -1, -1):
    if path[i][0] == parent:
        parent = path[i][1]
        print("To", path[i][0], "from", path[i][1])
