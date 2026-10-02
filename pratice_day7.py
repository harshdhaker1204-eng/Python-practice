"Print all numbers from 1 to 100 using a for loop"
# for i in range(1,101):
#     print(i  ,end=" ")

"Print all even numbers between 1 and 200"
# for i in range(2,200,2):
#     print(i , end=" ")
"Print all odd number between 1 and 200."
# for i in range(1,200,2):
#     print(i ,end=" ")
"Print the table of any number entered by the user"
# num=int(input("Enter a number"))

# for i in range(1,11):
#     print(f"{num} X {i} ={i*num}")
"Print the sum of numbers from 1 to N"

# num=int(input("Enter a number="))
# total=0

# for i in range(1,num+1):
#     total+=i
#     print(total)
"Print the Factorial of a number using a for loop."
# num=int(input("Enter a number"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
#     print("Factorial is",fact)

"Count how many vowels are in a given string using a for loop"
# str=input("Enter any character")
# Vowel="aeiouAEIOU"
# count=0
# for ch in str:
#     if ch in Vowel:
#      count+=1
#      print("Total vowels",count)
"Print each character of a string on a new using a loop"
# for i in "banana":
#     print(i)

"Find the largest number in a list using loop"

# lst = [12, 45, 7, 89, 23]

# largest = lst[0]   # first element ko assume kar lo sabse bada

# for num in lst:
#     if num > largest:
#         largest = num

# print("Largest number is:", largest)

"Print all numbers from 1 to N using a While loop"
# i=1
# num=int(input("Enter a number"))

# while i<=num:
#     print(i)
#     i+=1

"Print the sum of numbers from 1 to N using a while loop"
# i=1
# num=int(input("Enter a number"))
# total=0
# while i<=num:
#     total+=i
#     print(total)
#     i+=1

"Print all even numbers between 1 to 100 using while loop"
# i=1

# while i<=100:
#     if i%2==0:
#       print(i, end=" ")
#     i+=1

"Print all odd number between 1 and 100 using while loop"
# i=1
# num=30
# while i<num:
#     if i%2!=0:
#         print(i,end=" ")
#     i+=1

"Count how many digits are in a given number using while loop"
# num = int(input("Enter a number: "))

# count = 0
# while num > 0:
#     num = num // 10   # last digit remove
#     count += 1        # count increase

# print("Total digits:", count)

"Reverse  a number using while loop"
# num=int(input("Enter a number:"))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# print("Reversed number:",reverse)
"Check whether number is a palindrome usinf while loop"
# num=int(input("Enter a number"))
# original=num
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# if original == reverse:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")
"find the factorial of a number using a while loop"
# num=int(input("Enter a number"))

# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print("The factorial is",fact)
"Print the Multiplication table using a while loop"
# num=int(input("Enter a number:"))
# i=1
# while i<=10:
 
#   print(f"{num} X {i}={i*num}")
#   i+=1

"Find the largest digit in a number using a while loop"
# num=int(input("Enter a number"))
# largest=0

# while num > 0:
#     digit=num%10
#     if digit>largest:
#         largest=digit
#     num=num//10
# print("Largest digit is:",largest)
"Find the smallest digit in a number using a while loop"
# num = int(input("Enter a number: "))

# temp = num
# smallest = 9   # highest digit se start

# while temp > 0:
#     digit = temp % 10
#     if digit < smallest:
#         smallest = digit
#     temp = temp // 10

# print("Smallest digit is:", smallest)
"Count  how many vowels are in a string using a while loop(use indexing)"
# str=input("Enter a character")
# vowels="aieouAIEOU"
# count=0
# i=0
# while i <len(str):
#     if str[i] in vowels:
#         count+=1
#     i+=1
# print("Number of vowels",count)

"Print each character of astring one by one using while loop"
# string = input("Enter a string: ")

# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

"Print each character of string one by one using while loop"
# n=int(input("Enter number of terms"))
# a=0
# b=1
# count=0

# while count <n:1
#     print(a,end=" ")
#     c= a+b
#     a=b
#     b=c
#     count+=1
"Find the sum of digits of a number using a while loop"

num=int(input("Enter a number"))
total=0
while num>0:
    digit=num%10
    total+=digit
    num//=10
print("Sum of elements",total)

"Print numbers from N down to 1(reverse counting) using a while loop"
# num=int(input("Enter a number"))
# while num>=1:
#     print(num)
#     num-=1
"Print all multiples of 5 between 1 and 200 using a while loop"
# i=5
# while i<=200:
#     print(i)
#     i+=5
















