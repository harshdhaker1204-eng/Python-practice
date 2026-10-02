#using matrix representation
from collections import deque
# class Graph:
#     def __init__(self,vertex):
#         self.size=vertex
#         self.mat=[[0]*vertex for x in range(vertex)]
#     def add_edge(self,src,dest):
#         if 0<=src<self.size and 0<=dest<self.size:
#             self.mat[src][dest]=1
#             self.mat[dest][src]=1
#         else:
#             print("Invalid")
#     def print(self):
#         for row in self.mat:
#             print(''.join(map(str,row)))
#     def bfs(self,src):
#         visited=[False]*self.size
#         queue=deque([src])
#         visited[src]=True
#         while queue:
#             v=queue.popleft()
#             print(v,end=" ")
#             for i in range(self.size):
#                 if (self.mat[v][i]==1 and visited[i]==False):
#                     visited[i]=True
#                     queue.append(i)
# G=Graph(6)
# G.add_edge(1,2)
# G.add_edge(2,3)
# G.add_edge(1,4)
# G.add_edge(4,3)
# G.add_edge(2,4)
# G.add_edge(4,5)
# G.add_edge(2,5)
# G.bfs(1)

#using list representation
from collections import deque


class Graph:

    def __init__(self):
        self.adjlist = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        # Undirected graph
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)

    def print(self):
        for vertex in self.adjlist:
            print(vertex, "->", self.adjlist[vertex])

    def BFS(self, src):
        visited = set()
        queue = deque([src])

        visited.add(src)

        while queue:
            v = queue.popleft()
            print(v, end=" ")

            for i in self.adjlist[v]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


# Create graph
G = Graph()

# Add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 4)
G.add_edge(4, 3)
G.add_edge(2, 4)
G.add_edge(4, 5)
G.add_edge(2, 5)

# Print adjacency list
G.print()

# BFS starting from vertex 1
print("BFS:")
G.BFS(1)