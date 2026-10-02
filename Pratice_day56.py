"Pratice question no 1 write A pattern in python code"
# n = 6

# for i in range(n):
#     for j in range(n * 2):
        
#         # Left slant line
#         if j == n - i - 1:
#             print("*", end="")
        
#         # Right slant line
#         elif j == n + i - 1:
#             print("*", end="")
        
#         # Middle horizontal line
#         elif i == n // 2 and j > n - i - 1 and j < n + i - 1:
#             print("*", end="")
        
#         else:
#             print(" ", end="")
    
#     print()
"Pratice question no 2"
n=4
#upper part
# for i in range(n):
#     for j in range(n*2):
#         # boundary lines only
#         if j==n-i-1 or j==n+i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #Lower part
# for i in range(n-2,-1,-1):
#     for j in range(2*n-1):
#         if j==n-i-1 or j==n+i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

"Pratice question no 3"
n=4
#empty matrix
matrix=[[0]*n for _ in range(n)]
top=0
bottom=n-1
left=0
right=n-1

num=1
while top<=bottom and left <=right:
    #left -right
    for i in range(left,right+1):
        matrix[top][i]=num
        num+=1
    top+=1
    #top -bottom
    for i in range(top,bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1
    # right-left  
    if top<=bottom:
        for i in range(right,left-1,-1):
            matrix[bottom][i]=num
            num+=1
        bottom-=1
    #bottom -top
    if left <=right:
        for i in range(bottom,top-1,-1):
            matrix[i][left]=num
            num+=1
        left+=1
#print matrix
for row in matrix:
    print(*row)  
    
        





