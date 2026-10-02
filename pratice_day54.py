"question no 1"
# import math
# def print_primes(L,R):
#     for num in range(L,R+1):
#         if num<2:
#             continue
#         is_prime=True
#         for i in range(2,int(math.sqrt(num))+1):
#             if num%i==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             print(num)
# #Example
# print_primes(10,300)

"question no 2"

# def is_strong(n):
#     original=n
#     total=0

#     while n>0:
#         digit=n%10 #last digit 
#         n=n//10

#         #Factorial calculate using loop
#         fact=1
#         for i in range(1,digit+1):
#             fact*=i
#         total+=fact
#     if total == original:
#         print("Strong Number")
#     else:
#         print("Not strong number")
# #Example
# is_strong(145)

"Program no 3"
def hollow_pyramid(n):
    for i in range(1, n + 1):
        
        # spaces
        for s in range(n - i):
            print(" ", end="")
        
        # columns
        for j in range(1, 2 * i):
            
            if i == 1 or i == n or j == 1 or j == 2*i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        
        print()

# Example
hollow_pyramid(5)



