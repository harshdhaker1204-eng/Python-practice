
"Pratice question no 1 using for loop"
# num=int(input("Enter a number"))
# Even=0
# for i in range(num+1):
#     if i%2==0:
#         Even+=i
# print("Total sum of Even number",Even)

"Pratice question no 2 using while loop"
# num=int(input("Enter a number"))
# Even=0
# i=1
# while i<=num:
#     if i%2==0:
#         Even+=i
#     i+=1
# print("Total sum of Even number",Even)

"Pratice question no 3 using for loop"

# num = input("Enter a number: ")

# set1 = set()

# for i in num:
#     set1.add(int(i))

# lst = sorted(set1)

# print("Second largest element:", lst[-2])

"Pratice question no 4 using while loop"


# num = int(input("Enter a number: "))

# set1 = set()

# while num > 0:
#     digit = num % 10
#     set1.add(digit)
#     num = num // 10
# lst = sorted(set1)

# print("Second largest element:", lst[-2])

"Pratice question no 5 using while loop"
# num=int(input("Enter a number:"))
# temp=num
# digit_sum=0
# while temp>0:
#     digit=temp%10
#     digit_sum+=digit
#     temp//=10
# if num%digit_sum==0:
#     print("Harshad number")
# else:
#     print("Not a Harshad Number")

"Pratice question no 6 using for loop"

# num=int(input("Enter a number:"))
# for i in range(1,num+1):
#     temp=i
#     rev=0

#     while temp>0:
#         digit=temp%10
#         rev=rev*1+digit
#         temp=temp//10
#     if i==rev:
#         print(i)

"Pratice question no 7 using for loop"
# num=int(input("Enter a number"))
# count=0
# i=0
# while i<=num:
#     if (i%3==0 or i%7==0) and not (i%3==0 and i%7==0):
#         count+=1
#     i+=1
# print("Count=",count)

"Pratice question no 7 using for loop"

# num=1
# rows=4
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

"Pratice question no 8 using for loop"
# import string
# letter=ord('A')
# rows=4
# for i in range(1,rows+1):
#     for j in range(i):
#         print(chr(letter),end=" ")
#         letter+=1
#     print()

"Pratice question no 9 using for loop"
# largest=0
# while True:
#     num=int(input("Enter a number(0 to stop)"))
#     if num==0:
#         break
#     if num>largest:
#         largest=num
# print("Largest number",largest)

"Pratice question no 10 using for loop"
# num=int(input("Enter a number:"))
# sum_div=0
# i=1
# while i<num:
#     if num%i==0:
#         sum_div+=i
#     i+=1
# if sum_div== num:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

"Pratice question no 11 using for loop"
# n=int(input("Enter N:"))
# for num in range(1,n+1):
#     cout=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count!=2:
#         print(num)










    





    












