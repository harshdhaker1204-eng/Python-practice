"pratice question no 1"
# def merge_dictionary(d1,d2):
#     d3={}
#     for i in d1:
#       d3[i]=d1[i]
#     for i in d2:
#        d3[i]=d2[i]
#     return d3
# d1={1:"Rohit",2:"Arjune",3:"Rahul"}
# d2={4:"Vishal",5:"Dilip",7:"Kanishk"}
# print(merge_dictionary(d1,d2))

"pratice question no 2"

# def swap_value(d1):
#     rev={}
#     for key,val in d1.items():
#         rev[val]=key
#     return rev
# d1={1:"Rohit",2:"Arjune",3:"Rahul"}
# print(swap_value(d1))

"pratice question no 3"
# def count_word(n):
#     return len(n.split())
# print(count_word("My name is baba tilu"))

"pratice question no 4"
# import math
# def GCD(n1,n2):
#     return math.gcd(n1,n2)
# print(GCD(18,36))
"pratice question no 5"
# import math
# def LCM(n1,n2):
#     return math.lcm(n1,n2)
# print(LCM(18,36))

"pratice question no 6"
# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1)+fibo(n-2)
# print(fibo(8))

"pratice question no 7"
# def Binary_Search(A,low,high,target):
#     if low>high:
#         return -1
#     mid=low+(high-low)//2
#     if A[mid]==target:
#         return mid
#     elif target<A[mid]:
#         return Binary_Search(A,low,mid-1,target)
#     else:
#         return Binary_Search(A,mid+1,high,target)
# low=1
# high=8
# target=9
# A=[1,2,3,4,5,6,7,8,9]
# print(Binary_Search(A,low,high,target))

"pratice question no 8"
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

"pratice question no 9"
# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")

class Solution: 
    def checkDivisibility(self, n: int) -> bool: 
        sum1 = 0

        for i in int(n):
            sum1 += i

        print(sum1)


#         for j in range(n):
#             product*=j
#         SP=product+sum1
#         if n==SP:
#             return True
#         return False
S=Solution()
P=S.checkDivisibility(99)
print(P)