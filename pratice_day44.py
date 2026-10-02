"Pratice question no 1 using for loop"
# for i in range(100):
#      print(i)
"Pratice question no 1 using while loop"
# n=100
# i=1
# while i<=100:
#     print("-",i)
#     i+=1
"Pratice question no 2 using for loop"
# for i in range(2,50,2):
#     print("=",i)
"Pratice question no 2 using while loop"
# n=50
# i=2
# while i<=50:
#     print("-",i)
#     i+=2
"Pratice question no 3 using for loop"
# for i in range(1,50,2):
#     print("This is odd number",i)
"Pratice question no 3 using while loop"
# n=50
# i=1
# while i<=50:
#     print("odd numbers",i)
#     i+=2
"Pratice question no 4 using for loop"
# num=int(input("Enter a number="))
# sum=0
# for i in range(num+1):
#     sum+=i
# print("The sum of natural number are",sum)

"Pratice question no 4 using while loop"
# num=int(input("Enter a number="))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1
# print("The Sum of n natural number are",sum)
"Pratice question no 5 using for loop"
# num=int(input("Enter a number="))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print("The factorial is",fact)

"Pratice question no 5 using while loop"
# num=int(input("Enter a number="))
# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print("The factorial is",fact)

"Pratice question no 6 using for loop"
# for i in range(1,100):
#     if i%5==0:
#         continue
#     print(i)
"Pratice question no 6 using while loop"
# num=100
# i=1
# while i<=num:
#     if i%5==0:
#          i+=1
#          continue
   
#     print("-",i)
#     i+=1
"Pratice question no 7 using for loop"
# for i in range(1,101):
#     if ((i%3==0) and (i%5==0)):
#         print(i,"This number divisible by both 3 and 5")

"Pratice question no 7 using while loop"
# num=100
# i=1
# while i <= num:
#     if (i % 3 == 0) and (i % 5 == 0):
#         print(i, "This number divisible by both 3 and 5")
#     i += 1

"Pratice question no 8 using for loop"
# num=5

# for i in range(1,11):
#    print(f"{num} X {i} =",num*i)

"Pratice question no 8 using while loop"

# num=5
# i=1
# while i<=10:
#     print(f"{num} X {i} =",num*i)
#     i+=1

"Pratice question no 9 using for loop"
# for i in range(10,0,-1):
#     print(i)

"Pratice question no 9 using while loop"
# i=10
# while i>=1:
#     print(i,end=" ")
#     i-=1

"Pratice question no 10 using for loop"
# for i in range(1,100):
#     if i==7:
#         break
#     print(i)

"Pratice question no 10 using while loop"
# num=100
# i=1
# while i<=num:
#     if i==8:
#         break
#     print(i,end=" ")
#     i+=1

"Pratice question no 11 using for loop"
# num=int(input("Enter a number"))

# if num<=1:
#     print("Not a prime number")

# else:

#     for i in range(2,num):
#         if num%i==0:
#            print("Not a prime number")
#            break
#     else:
#         print("Prime number")

"Pratice question no 11 using while loop"
# num=int(input("Enter a number"))
# i=2
# while i*i<=num:
#     if num%i==0:
#         print("Not a prime number")
#         break
#     i+=1

# else:
#     if num>1:
#         print("prime number")
#     else:
#         print("Nota prime number")

"Pratice question no 12 using for loop"
# print("prime number from 1 to 100")

# for num in range(2,101):
#      is_prime=True
#     #  for i in range(2,int(num**0.5)+1):
#      for i in range(2,num): 
#           if num%i==0:
#                is_prime=False
#                break
#      if is_prime:
#           print(num,end=" ")

"Pratice question no 12 using while loop"          
# num=2
# while num<=100:
#      is_prime=True
#      i=2
#      while i<num:
#           if num%i==0:
#                is_prime =False
#                break
#           i+=1
               
#      if is_prime:
#           print(num,end=" ")
#      num+=1

"Pratice question no 13 using for loop"

# num=int(input("Enter a number"))          
# rev=0
# for i in range(len(str(num))):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print("The reverse number is",rev)

"Pratice question no 13 using while loop"

# num=int(input("Enter a number"))          
# rev=0

# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
    
# print("The reverse number is",rev)

"Pratice question no 14 using for loop"
# num=int(input("Enter a number"))
# origanal=num
# rev=0
# for i in range(len(str(num))):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if origanal==rev:
#     print("Its palindrome ")
# else:
#     print("Its not a palindrome ")

"Pratice question no 14 using while loop"
# num=int(input("Enter a number"))
# origanal=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if origanal==rev:
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")


"Pratice question no 15using for loop"
# num=int(input("Enter a number"))
# sum=0
# for i in range(len(str(num))):
#     digit=num%10
#     sum+=digit
#     num//=10
# print("The sum of digit are ",sum)

"Pratice question no 15 using while loop"
# num=int(input("Enter a number"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num//=10
# print("The sum of digits are ",sum)

"Pratice question no 16 using for loop"
# num=int(input("Enter a number"))
# product=1
# for i in range(len(str(num))):
#     digit=num%10
#     product*=digit
#     num//=10
# print("The product of digits are",product)

"Pratice question no 16 using while loop"
# num=int(input("Enter a number"))
# product=1
# while num>0:
#     digit=num%10
#     product*=digit
#     num//=10
# print("The product of digits are",product)


"Pratice question no 17 using for loop"
# num=int(input("Enter a number"))

# for i in range(1,num+1):
#     square=i**2
#     print(f"the  square of {i} is {square}")  

"Pratice question no 17 using while loop"
# num=int(input("Enter a number"))
# i=1
# while i<=num:
#     print(i**2)
#     i+=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              