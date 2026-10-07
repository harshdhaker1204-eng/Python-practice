# from collections import deque
# class Node:
#     def __init__(self,vertex):
#         self.mat=[[0] * vertex for x in range(vertex)]
#     def add_edge(self,sor,des):
#         if 0<sor<=len(self.mat) or 0<des<len(self.mat):
#             self.mat[sor][des]=1
#             self.mat[des][sor]=1
#         else:
#             print("Invalid matrix")
#     def print(self):
#         for row in self.mat:
#             print(''.join(map(str,row)))
#     def bfs(self,sor):
#         visited=[False]*len(self.mat)
#         queue=deque([sor])
#         visited[sor]=True
#         while queue:
#             v=queue.popleft()
#             print(v,end=" ")
#             for i in range(len(self.mat)):
#                 if self.mat[v][i]==1 and visited[i]==False:
#                     visited[i]=True
#                     queue.append(i)

# G=Node(5)
# G.add_edge(1,4)
# G.add_edge(1,3)
# G.add_edge(0,1)
# G.add_edge(4,2)
# G.print()
# G.bfs(0)
        
class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for x in  range(vertex)]
    def add_edge(self,sor,dest):
        if 0<sor<=len(self.mat) or 0<dest<=len(self.mat):
            self.mat[sor][dest]=1
            self.mat[dest][sor]=1
        else:
            print("Invalid node")
    def print(self):
        for row in self.mat:
            print(''.join(map(str,row)))
    def dfs(self,sor):
        visited=[False]*len(self.mat)
        stack=[sor]
        while stack:
            v=stack.pop()
            if visited[v]==False:
                print(v,end="->")
                visited[v]=True
            for i in range (len(self.mat)):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
            
G=Graph(5)
G.add_edge(1,4)
G.add_edge(1,3)
G.add_edge(0,1)
G.add_edge(4,2)
G.print()
G.dfs(0)
                   