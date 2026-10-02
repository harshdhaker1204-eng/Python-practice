# class Graph:
#     def __init__(self,vertex):
#         self.size=vertex
#         self.mat=[[0]*vertex for x in range(vertex)]
#     def add_egde(self,src,dest):
#         if 0<=src<self.size and 0<=dest<self.size:
#             self.mat[src][dest]=1
#             self.mat[dest][src]=1
#         else:
#             print("Invalid")
#     def print(self):
#         for row in self.mat:
#             print(''.join(map(str,row)))
#     def dfs(self,src):
#         visited=[False]*self.size
#         stack=[src]
#         while stack:
#             v=stack.pop()
#             if not visited[v]:
#                print(v,end="->")
#                visited[v]=True
#             for i in range(self.size-1,-1,-1):
#                 if self.mat[v][i]==1 and visited[i]==False:
#                    stack.append(i)

# g=Graph()
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(1,4)
# g.addEdge(4,3)
# g.addEdge(2,4)
# g.addEdge(4,5)
# g.addEdge(2,5)
# # G.print()
# g.dfs(0)

        


import pandas as pd
data=["2025-01-10","2025-02-15","wrong_date"]
dt=pd.to_datetime(data,errors="coerce")
print(dt)
print(data)


