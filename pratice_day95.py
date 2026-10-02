from collections import deque
n=5
edges=[[0,1],
       [0,2],
       [1,3],
       [1,4]]
#create adjacency list
adj=[[] for _ in range(n)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
print("Adjacency list:")
for i in range(n):
    print(i,"->",adj[i])
#Tree must have n-1 edges
if len(edges)!=n-1:
    print("False")
else:
    visited=set()
    queue=deque()
    queue.append(0)
    visited.add(0)
    while queue:
        node=queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    if len(visited)==n:
        print("True")
    else:
        print("False")
        