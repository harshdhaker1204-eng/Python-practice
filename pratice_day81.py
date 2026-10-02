"Pratice question no 1"
# start=1
# end=100000
# for num in range(start,end+1):
#     temp=num
#     total=0
#     while temp>0:
#         digit=temp%10
#         fact=1
#         for i in range(1,digit+1):
#             fact*=i
#         total+=fact
#         temp//=10
#     if num==0:
#         total=1
#     if total==num:
#         print(num)
"Pratice question no 2"
# n=5
# #upper half
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     print("*",end="")
#     if i>0:
#         for j in range(2*i-1):
#             print(" ",end="")
#         print("*",end="")
#     print()
# #Lower Half
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     print("*",end="")
#     if i>0:
#         for j in range(2*i-1):
#             print(" ",end="")
#         print("*",end="")
#     print()
"Pratice question no 3"
# n=5
# for i in range(4):
#     print("*")
# for i in range(5):
#     print("*",end=" ")

"Pratice question no 1"
n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
           print("*",end="")
        else:
            print(" ",end="")
    print()