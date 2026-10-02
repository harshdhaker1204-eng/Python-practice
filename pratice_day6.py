"Print numbers from 1 to 100 using a loop"
# for x in range(1,101):
#     print(x )
"Print all even numbers between 1 and 50."
# for x in range(2,51,2):
#     print(x ,end=" ")
"Print all odd numbers from 1 to 100"
# for x in range(1,50,2):
#     print(x,end=" ")
"Print the multiplication table of any number entered by the user"
# num=int(input("Enter your number:"))
# for x in range(1,11):
#     print(f"{num}*{x}={num*x}")
"Find the sum of the first N natural numbers"
# N=int(input("Enter any positive number"))

# if N>0:
#     total=0
#     for x in range(1,N+1):
#          total+=x
#          print("Sum of first",N ," Natural Numbers is",total)
# else:
#     print("invalid negative number please Enter positive number")

"Find the factorial of a given numbers"
# num=int(input("Enter a number"))


# fact=1
# for i in range(1,num+1):
#     fact*=i
#     print("factorial is",fact)

"Count how many digits are in a given number"
# num = input("Enter a number: ")

# count = 0

# for digit in num:
#     count += 1

# print("Number of digits:", count)

"Reverse a number using a loop(no string method)"
# num=int(input("Enter a number"))

# rev=0
# temp=num
# for i in range(rev):
#       digit = temp % 10
#       rev = rev * 10 + digit
#       temp //= 10

# print("Reversed number is:", rev)

"Print the fibonacci series for N terms"

# num=int(input("Enter a number"))
# a=0
# b=1

# for i in range(num):
   
#     print(a ,end=" ")
#     c=a+b
#     a=b
#     b=c


"Print all numbers that are divisible by both 3 and 5  between 1 and 200"

# for i in range(1,201):
#     if i%3==0 and i%5==0:
#         print(i)

# for i in range(15,201,15):
#     print(i)

"print the sum of digits of a number using a loop"

# num = input("Enter a number: ")

# total = 0
# for digit in num:
#     total += int(digit)

# print("Sum of digits =", total)

"Check if a number is prime using a loop."
# num=int(input("Enter a number"))

# if num<=1:
#     print("Not a prime number")
# else:

#     for i in range(2,num):

#         if num %i==0:
#          print("Not a prime number")
#          break
#         else:
#            print("Prime number")

"Print this pattern"
"*"
"**"
"***"
"****"
"*****"

# for i in range(1,6):
#     for j in range(i):
#       print("*",end=" ")
#     print()

"Print this reverse pattern"
"* * * * *"
"* * * *"
"* * *"
"* *"
"*"
# r=6
# for i in range(r):
#     for j in range(i,r-1):
#         print("*",end=" ")
#     print()

"print all characters of a string using a loop"

# for i in "banana":
#     print(i)

"Count vowels and consonants in a string"
# text=input("Enter a string:")
# Vowels_List="aieouAIEOU"
# vowels=0
# consonants=0

# for ch in text:
#     if ch.isalpha():
#         if ch in Vowels_List:
#             vowels+=1
#     else:
#         consonants+=1
# print("Vowels:",vowels)
# print("Consonants:",consonants)

"Print the square of all numbers from 1 to N"

# num=int(input("Enter a number"))

# for i in range(1,num+1):
#     print(i*i)

"Display the largest digit in a number using a loop"

# num = input("Enter a number: ")

# largest = 0

# for ch in num:
#     digit = int(ch)
#     if digit > largest:
#         largest = digit

# print("Largest digit:", largest)
"Print all element of a list using a loop."
# l1=[1,2,3,4,5,6,7,8,9,10]

# for i in l1:
#     print(i)


"Find how many numbers in a list are positive.negative,and zero"
# l1=[-1,2,0,3,4,-5,0,6]
# positive=0
# negative=0
# zero=0
# for i in l1:
#     if i>0:
#         positive+=1
#     elif i<0:
#         negative+=1
#     else:
#         zero+=1

# print("Positive numbers",positive)
# print("Neagtive numbers",negative)
# print("ZerosNumbers",zero)



  


