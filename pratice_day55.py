"Pratice question no 1"
# def is_prime_number(x):
#     if x<=1:
#         return False
#     else:
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#     return True
# print(is_prime_number(6)) 

"Pratice question no 2"
# n=int(input("Enter a n"))


# for num in range(2,n+1):
#     is_prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#            print(num,end=" ")

       
"Pratice question no 3"
# def check_armstrong_number(x):
#     original=x
#     armstrong_number=0
#     while x>0:
#         digit=x%10
#         armstrong_number+=digit**3
#         x//=10
#     if original==armstrong_number:
#         print("Its armstrong number")
#     else:
#         print("Its not armstrong number")
# print(check_armstrong_number(153)) 

"Pratice question no 4"
# def one_to_n_number_of_arm_strong_number(x):
#     result=[]
#     for i in range(x+1):
#         num=i
#         arm_strong=0
#         while num>0:
#           digit=num%10
#           arm_strong+=digit**3
#           num//=10
#         if i==arm_strong:
#            result.append(i)
#     return result
# print(one_to_n_number_of_arm_strong_number(1000))

"Pratice question no 5"
# for i in range(5):
#     if i<4:
#         print("*")
#     else:
#        for j in range(5):
#          print("*",end= " ")


















        
                