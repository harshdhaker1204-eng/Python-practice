from collections import deque
# class Graph:
#     def __init__(self):
#         self.adjlist={}
#     def add_vertex(self,vertex):
#         if vertex not in self.adjlist:
#             self.adjlist[vertex]=[]
#     def (self,src,dest):
#         self.add_vertex(src)
#         self.add_vertex(dest)
#         self.adjlist[src].append(dest)
#         self.adjlist[dest].append(src)
#     def printgraph(self):
#         for vertex in self.adjlist:
#             print(vertex,"->",self.adjlist[vertex])
#     def bfs(self,src):
#         visited=[False]*(max(self.adjlist)+1)
#         queue=deque([src])
#         visited[src]=True
#         while queue:
#             v=queue.popleft()
#             print(v,end="->")
#             for nei in self.adjlist[v]:
#                 if not visited[nei]:
#                     queue.append(nei)
#                     visited[nei]=True
# g=Graph()
# g.(1,2)
# g.(2,3)
# g.(1,4)
# g.(4,3)
# g.(2,4)
# g.(4,5)
# g.(2,5)
# g.printgraph()
# g.bfs(1)

class Graph:
    def __init__(self):
        self.adjlist={}
    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex]=[]
    def add_edges(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)
    def printGraph(self):
        for vertex in self.adjlist:
            print(vertex,"->",self.adjlist[vertex])
    def dfs(self,src):
        visited=[False]*(max(self.adjlist) + 1)
        stack=[src]
        while stack:
            v=stack.pop()
            if visited[v]==False:
                print(v,end="->")
                visited[v]=True
            for nei in self.adjlist[v]:
                if visited[nei]==False:
                    stack.append(nei)
g=Graph()
g.add_edges(1,2)
g.add_edges(2,3)
g.add_edges(1,4)
g.add_edges(4,3)
g.add_edges(2,4)
g.add_edges(4,5)
g.add_edges(2,5)
g.printGraph()
g.dfs(1)