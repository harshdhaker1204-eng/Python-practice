"1 to N number print by using for loop"
# num=int(input("Enter a number"))
# for i in range(num):
#     print(i,end=" ")
"1 to N number print by using while loop"
# num=int(input("Enter a number"))
# i=1
# while i<=num:
    
#     print(i,end=" ")
#     i+=1
"N to 1 number print by using for loop"
# num=int(input("Enter a number"))
# for i in range(num,0,-1):
#     print(i,end=" ")
"N to 1 number print by using wjile loop"
# num=int(input("Enter a number"))
# i=num
# while i>=1:
#     print(i,end=" ")
#     i-=1
"1 to 100 print odd number using for loop"
# for i in range(1,101,2):
#     print(i)
"1 to 100 print odd number using while loop"
# i=1
# while i<=100:
#     print(i)
#     i+=2
"1 to 100 print Even number using for loop"

# for i in range(2,101,2):
#     print(i)
"1 to 100 print Even number using while loop"
# i=2
# while i<=100:
#     print(i)
#     i+=2
"print square 1 to N using while loop"
# num=int(input("Enter a number"))
# i=1
# while i<=num:
#     print(i*i,end=" ")
#     i+=1
"print square 1 to N using for loop"
# num=int(input("Enter a number"))

# for i in range(num):
#     print(i*i)

"1 to N number sum using while loop"
# i=1
# num=int(input("Enter a number"))
# total=0
# while i<=num:
#     total+=i
#     print(total)
#     i+=1
"1 to N number sum using for loop"

# num=int(input("Enter a number"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
#     print(sum)
#     i+=1

"Find the factorial number using for loop"
# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print("Factorial =", fact)

"Find the factorial number using for loop"
# num = int(input("Enter a number: "))
# fact = 1
# while num>=0:
#     fact*=num
#     num+=1
# print("factorial",fact)
"Print 5 divisible number 1 to 100 using for loop"
# for i in range(5,100,5):
#     print(i,end=" ")

"Print 5 divisible number 1 to 100 using while loop"

# i=5
# while i<=100:
#     print(i,end=" ")
#     i+=5
"count digit in number using for loop"
# num = (input("Enter a number: "))
# count=0
# for i in num:
#     count+=1
#     print(count)

"count digit in number using while loop"

# num = int(input("Enter a number: "))
# count = 0

# while num > 0:
#     count += 1
#     num //= 10

# print("Total digits =", count)
"Reverse number using loop"
# Number = 123
# rev = 0

# while Number > 0:
#     digit = Number % 10
#     rev = rev * 10 + digit
#     Number //= 10

# print(rev)
"Sum of digits"
# def sum_of_digits(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10
#     return total

# print(sum_of_digits(1234))

# 

# def count_vowels(character):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for ch in character:
#         if ch in vowels:
#             count += 1
#     return count

# print(count_vowels("Harsh"))     # 1
# print(count_vowels("aaaaee"))    # 6

"Factorial function"
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# print(factorial(5))


"Check prime number or not"
# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(is_prime(7))
# print(is_prime(4))