"Pratice question no 1"
# n=5
# #upper Half
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     for j in range(2 * (n-i)):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# #Lower Half
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     for j in range(2 *(n-i)):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

"Pratice question no 2"
# n=5
# i=1
# #Upper case
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     space=1
#     while space<2*(n-i):
#         print(" ",end="")
#         space+=1
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1
# #Lower case
# i=n-1
# while i>=1:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     space=1
#     while space<2*(n-i):
#         print(" ",end="")
#         space+=1
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i-=1


"Pratice question no 3"
# n = 5

# # Upper Half
# for i in range(1, n + 1):

#     # Leading spaces
#     for j in range(n - i):
#         print(".", end="")

#     # Stars
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(".", end="")

#     print()

# # Lower Half
# for i in range(n - 1, 0, -1):

#     # Leading spaces
#     for j in range(n - i):
#         print(".", end="")

#     # Stars
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(". ", end="")

#     print()
"Pratice question no 4"
# n=5
# i=1
# while i<=n:
#     space=0
#     while space<n-i:
#         print(".",end="")
#         space+=1
#     j=0
#     while j<2*i-1:
#         if j==0 or j==2*i-2:
#             print("*",end="")
#         else:
#             print(".",end="")
#         j+=1
#     print()
#     i+=1
# i=n-1
# while i>=1:
#     space=0
#     while space<n-i:
#         print(".",end="")
#         space+=1
#     j=0
#     while j<2*i-1:
#         if j==0 or j==2*i-2:
#             print("*",end="")
#         else:
#             print(".",end="")
#         j+=1
#     print()
#     i-=1

"Pratice question no 5"
# n=5
# for i in range(1,n+1):
#     #space 
#     for j in range(n-i):
#         print("*",end="")
#     #Descending Numbers
#     for j in range(i,0,-1):
#         print(j,end="")
#     #Ascending numbers
#     for j in range(2,i+1):
#         print(j,end="")
#     print()

"Pratice question no 6"
# n=5
# i=1
# while i<=n:
#     space=0
#     while space<n-i:
#         print(".",end="")
#         space+=1
#     #Decending numbers
#     j=i
#     while j>0:
#         print(j,end="")
#         j-=1
#     j=2
#     while j<i+1:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1

"Pratice question no 7"
# n = 5

# # Top line
# print("*" * (2 * n - 1))

# # Upper half
# for i in range(1, n):
#     print(" " * (i - 1) + "*" +
#           " " * (2 * (n - i) - 1) + "*")

# # Middle
# print(" " * (n - 1) + "*")

# # Lower half
# for i in range(n - 1, 0, -1):
#     print(" " * (i - 1) + "*" +
#           " " * (2 * (n - i) - 1) + "*")

# # Bottom line
# print("*" * (2 * n - 1))


"Pratice question no 8"
n=5
#Top line
# print("*"*(2*n-1))
#Upper half
# i=1
# while i<=n:
    
#     print(" " * (i - 1) + "*" +
#           " " * (2 * (n - i) - 1) + "*")
#     i+=1
# #Middle
# print(" " * (n-1) + "*")

# #Lower half
# i=n
# while i>0:
#     print(" " * (i - 1) + "*" +
#           " " * (2 * (n - i) - 1) + "*")
#     i-=1
# "Bottom line"
# print("*" * (2*n-1))


"Pratice question no 8"
# n=6
# for i in range(n):
#     #print leading spaces
#     for j in range(n-i-1):
#         print("*",end="")
#     num=1

#     #print Pascal Triangle values
#     for j in range(i+1):
#         print(num,end=" ")
#         num=num*(i-j) //(j+1)
#     print()
"Pratice question no 9"
# n=5
# #upper half
# for i in range(1,n+1):
#     #left wing
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end="")
#         else:
#             print(" ",end="")
# #     #Middle Space
#     for j in range(2*(n-i)):
#         print(" ",end="")
#     #Right wing
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end="")
#         else:
#             print(".",end="")
#     print()
# # #Lower Half
# for i in range(n,0,-1):
#     #left wing
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     #middle spaces
#     for j in range(2*(n-i)):
#         print(" ",end="")
#     #Right wing 
#     for j in range(1,i+1):
#         if j == 1 or j==i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    
# cook your dish here
for i in range(4):
    for j in range(4):
        print("*",end="")
    print()