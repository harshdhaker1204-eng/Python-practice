# matrix representation
# class Graph:
#     def __init__(self,vertex):
#         self.mat=[[0]*vertex for x in range(vertex)]
#     def add_edge(self,source,dest):
#         if 0<=source<len(self.mat) and 0<=dest<len(self.mat):
#             self.mat[source][dest]=1
#             self.mat[dest][source]=1
#         else:
#             print("Invalid Edge")
#     def print(self):
#         for row in self.mat:
#             print(" ".join(map(str,row)))
# g=Graph(5)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(3,4)
# g.add_edge(2,3)

# g.print()
        
"Graph representation by list"
# class Graph:
#     def __init__(self):
#         self.adjlist={}
#     def add_vertex(self,vertex):
#         if vertex not in  self.adjlist:
#             self.adjlist[vertex]=[]
#     def addEdge(self,src,dest):
#         self.add_vertex(src)
#         self.add_vertex(dest)
#         self.adjlist[src].append(dest)
#         self.adjlist[dest].append(src)
#     def print(self):
#         for vertex in self.adjlist:
#             print(vertex,"->",self.adjlist[vertex])
# g=Graph()
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(1,4)
# g.addEdge(4,3)
# g.addEdge(2,4)
# g.addEdge(4,5)
# g.addEdge(2,5)
# g.print()

