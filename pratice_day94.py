class Graph:
    def __init__(self,vertex):
        self.size=vertex
        self.adjlist={}
    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex]=[]
    def add_edge(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)
    def print(self):
        for vertex in self.adjlist:
            print(vertex,"->",self.adjlist[vertex])
    def dfs(self,src):
        visited=[False]*self.size
        stack=[src]
        while (stack):
            v=stack.pop()
            if visited[v]==False:
                print(v,end="->")
                visited[v]=True
            for i in self.adjlist[v]:
                if visited[i]==False:
                    stack.append(i)

g=Graph(6)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(4,3)
g.add_edge(2,4)
g.add_edge(4,5)
g.add_edge(2,5)
g.print()
print("DFS")
g.dfs(1)
       