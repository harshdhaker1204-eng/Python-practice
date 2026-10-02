"Sum or two numbers"
# def Sum_of_numbers(num1,num2):
#     return num1 + num2

# a = int(input("Enter num1 = "))
# b = int(input("Enter num2 = "))
    

# print("The sum of two numbers is:", Sum_of_numbers(a,b))

"Check even or odd"
# def Even_or_odd(num):
#     if num%2==0:
#         return "Even number"
#     else:
#         return "Odd number"
# a=int(input("Enter a number"))
# print(Even_or_odd(a))
"Find Maximum of three Numbers"
# def maximum_num(a,b,c):
#     if a>b and a>c:
#         return "a is greater then  b and c"
#     elif b>a and b>c:
#         return "b is greater then a and c"
#     elif c>a and c>b:
#         return " c is greater thean a and b"
#     else:
#         return "both three numbers are equal"
# num1=int(input("Enter a ="))
# num2=int(input("Enter b ="))
# num3=int(input("Enter c ="))
# print(maximum_num(num1,num2,num3))
"count Vowels in string"
# def count_vowels(str1):
#     vowels="aeiouAEIOU"
#     count=0
#     for ch in str1:
#         if ch  in vowels:
#             count+=1
#     return count

# char=input("Enter a string:")
# print("Number of vowels:",count_vowels(char))

"Factorial of a Number"
# def fact_of_number(num):
#     fact=1
   
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# factorial=int(input("Enter a number"))
# print("The Factorial is",fact_of_number(factorial))

"using while loops"
# def fact_of_number(num):
#     fact=1
#     i=1
   
#     while num>=i:
#         fact*=i
#         i+=1
#     return fact
# factorial=int(input("Enter a number"))
# print("The Factorial is",fact_of_number(factorial))

"Palindrome check"
# def is_palindrome(num):
#     original = num
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10

#     if original == rev:
#         return "Its palindrome"
#     else:
#         return "Not palindrome"


# a = int(input("Enter a number: "))
# print(is_palindrome(a))

"use for both cases "
# def is_palindrome(value):
#     value = str(value)      # number ho ya string → string bana do
#     return value == value[::-1]
# # Number check
# num = int(input("Enter a number: "))
# print("Palindrome" if is_palindrome(num) else "Not Palindrome")

# # String check
# text = input("Enter a string: ")
# print("Palindrome" if is_palindrome(text) else "Not Palindrome")

"Prime Number check"
# def is_prime_number(num):
    
#         if num<=1:
#             return False
#         for i in range(2,num):
#             if num%i==0:
#                return False
#         return True
        
# a=int(input("Enter a number"))
# print(is_prime_number(a))

"Reverse a Number"
# def rev_num(num):
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     return rev
# number=int(input("Enter a number"))
# print(rev_num(number))

"Sum of digits"
# def sum_of_digits(num):
#     total=0
    
#     while num>0:
#         digit=num%10
#         total+=digit
#         num//=10
#     return total
        
# number=int(input("Enter a digits:"))
# print(sum_of_digits(number))

"Count Even and odd numbers in List"
def count_even_odd(lst):
    even = 0
    odd = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_count, odd_count = count_even_odd(numbers)

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)




