"Sum of two number"
# def sum_of_two_numbers(num1,num2):
#     return num1+num2
# a=int(input("ENter a number a"))
# b=int(input("enter a number b"))
# print(sum_of_two_numbers(a,b))
"Even or odd"
# def Even_odd(lst):
#     Even=0
#     odd=0
#     for num in lst:
#         if num%2==0:
#             Even+=1
#         else:
#             odd+=1
#     return Even,odd
    
    
# a=[1,2,3,4,5,6,7,8]
# print(Even_odd(a))

"Factorial of a Number"
# def factorial_of_a_number(num):
#     fact=1
#     i=1
#     while num>=i:
#         fact*=i
#         i+=1
#     return fact
# a=int(input("Enter a factorial number="))
# print(factorial_of_a_number(a))
# def is_palindrome(value):
#     value = str(value)      # number ho ya string → string bana do
#     return value == value[::-1]
# # Number check
# num = int(input("Enter a number: "))
# print("Palindrome" if is_palindrome(num) else "Not Palindrome")

# # String check
# text = input("Enter a string: ")
# print("Palindrome" if is_palindrome(text) else "Not Palindrome")
"count digits in a number"
# def count_digit_in_a_number(num):
#     count =0
#     while num>0:
#         digit=num%10
#         count+=1
#         num=num//10
#     return count
# a=int(input("Enter a number"))
# print(count_digit_in_a_number(a))
"Prime number check"
# def is_prime_number(num):
    
#     if num<=1:
#         return "Not a prime number"
#     i=2
#     while num>i*i:
#         if num%i==0:
#             return  "Not a prime number"
#         i+=1
#     return "Prime number"
# a=int(input("Enter a number"))
# print(is_prime_number(a))

"Reverse a number"
# def reverse_num(num):
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     return rev
# a=int(input("Enter a number a"))
# print(reverse_num(a))

"Sum of list"
# def sum_of_list(lst):
#     sum=0
#     for num in lst:
        
#         sum+=num
        
#     return sum
# a=[1,2,3,4,5,6,7,8,9,10]
# print(sum_of_list(a))

# def fibonacci_series(num):
#     first = 0
#     second = 1

#     for _ in range(num):
#         print(first, end=" ")
#         next = first + second
#         first = second
#         second = next


# n = int(input("Enter number of terms: "))
# fibonacci_series(n)
"Check Armstrong Number"
# def is_Armstrong_Number(num):
#     original = num
    
#     # Step 1: count digits
#     count_digits = 0
#     temp = num
#     while temp > 0:
#         count_digits += 1
#         temp //= 10

#     # Step 2: calculate power sum
#     temp = num
#     power_sum = 0
#     while temp > 0:
#         digit = temp % 10
#         power_sum += digit ** count_digits
#         temp //= 10

#     # Step 3: compare
#     if power_sum == original:
#         return True
#     else:
#         return False
# print(is_Armstrong_Number(153))   # True
# print(is_Armstrong_Number(123))   # False
# print(is_Armstrong_Number(9474))  # True


"check strong Number"
# def is_strong_number(num):
#     sum_fact = 0
#     temp = num

#     while temp > 0:
#         digit = temp % 10
#         fact = 1

#         for i in range(1, digit + 1):
#             fact *= i

#         sum_fact += fact
#         temp //= 10

#     if sum_fact == num:
#         return "Strong Number"
#     else:
#         return "Not a Strong Number"


# a = int(input("Enter a number: "))
# print(is_strong_number(a))

"Count in vowels string"
# def count_vowels(str1):
#     vowels="aeiouAEIOU"
#     count=0
#     for ch in str1:
#         if ch in vowels:
#             count+=1
#     return count
# character=input("Enter a string")
# print(count_vowels(character))
"find minimum"
# def find_minimum(lst):
#     i = 0
#     min_val = lst[0]

#     while i < len(lst):
#         if lst[i] < min_val:
#             min_val = lst[i]
#         i += 1

#     return min_val


# nums = [10, 4, 6, 2, 8]
# print(find_minimum(nums))
"check perfect number"
# def is_perfect(num):
#     total=0
#     for i in range(1,num):
#         if num%i==0:
#             total+=i
        
#     if total==num:
#         print("Perfect number")
#     else:
#         print("Not a perfect number")
# a=6
# print(is_perfect(6))

"Calculate power"
# def Calculate_power(x,n):
#     return x**n
# print(Calculate_power(3,3))
"Using loops"
# def calculate_power(x,n):
#     result=1
#     for i in range(n):
#         result=result*x
#     return result
# print(calculate_power(3,4))

"Count Even and odd number in list"
# def Even_odd(nums):
#     Even=0
#     Odd=0
#     for num in nums:
#       if num%2==0:
#           Even+=1
#       else:
#           Odd+=1
#     return Even,Odd
# Even_counts,odd_counts =Even_odd([1,2,3,4,5,6,7,8])
# print("Even number",Even_counts)
# print("Odd number",odd_counts)


"Remove Duplicates from list"
# def Remove_Duplicates(lst):
#     new_list=[]
#     for item in lst:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list
# nums=[1,2,3,4,1,2,3,4,4]
# print(Remove_Duplicates(nums))

"check anagram string"
# def is_anagram_string(s1,s2):
#     return sorted(s1) == sorted(s2)
# print(is_anagram_string("listen","silent"))
"Find second largest number in list"
# def second_largest(nums):
#     if len(nums) < 2:
#         return "Second largest possible nahi hai"

#     largest = second = float('-inf')

#     for num in nums:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num

#     return second

# print(second_largest([10, 5, 20, 8, 15]))



    
