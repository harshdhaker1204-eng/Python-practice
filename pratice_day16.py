"Sum of Even Number in a list "
# def sum_even_number(num):
#     sum=0
#     for i in num:
#         if i%2==0:
#             sum+=i
#     return sum
# li=[1,2,3,4,5,6,7,8,9,10]
# print(sum_even_number(li))

"Sum of odd numbers"
# def sum_of_odd_number(li):
#     i = 0
#     total = 0
#     while i < len(li):
#         if li[i] % 2 != 0:
#             total += li[i]
#         i += 1
#     return total

# li = [1,2,3,4,5,6,7,8,9,10]
# print(sum_of_odd_number(li))
"Check Leap Year"
# def is_leao_year(year):
#     if (year%4 == 0) and (year%100!=0) or (year%400==0):
#         return "Leap year "
#     else :
#         return "Not a Leap year"
# print(is_leao_year(2000))
"Count words in a string"
# def count_word(word):
#     count_words=0
#     for ch in word:
#         count_words+=1
#     return count_words
# print(count_word("Harsh"))

"Using while loop"
# def count_words(words):

#     count=0
#     i=0
#     while i<len(words):
#         count+=1
#         i+=1
#     return count
# print(count_words("Harsh"))

"find common Elements in two lists"
# def common_element(l1, l2):
#     common = []
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 if i not in common:   # duplicate avoid
#                     common.append(i)
#     return common

# l1 = [1,2,3,4,5]
# l2 = [5,6,7,8,9,1]
# print(common_element(l1, l2))

"Check Number is positive ,Negative or zero"
# def is_number_positive_negative_or_zero(num):
#     if num>0:
#         return "positive"
#     elif num<0:
#         return "Negative"
#     else:
#         return "zero"
# print(is_number_positive_negative_or_zero(1))
# print(is_number_positive_negative_or_zero(-1))
# print(is_number_positive_negative_or_zero(0))

# def frequency(lst, element):
#     count = 0
#     for i in lst:
#         if i == element:
#             count += 1
#     return count

# nums = [1,2,3,4,5,6,7,8,7,7,7,7,7,7]

# print(frequency(nums, 7))

"Convert Celsius to Fahrenheit"
# def celsius_to_Fahrenheit(celsius):
#     Fahrenheit=(celsius*9/5)+32
#     return Fahrenheit
# print(celsius_to_Fahrenheit(100))
 
"Find lenght of string(Without len)"
# def find_length(words):
#     counts=0
#     for ch in words:
#         counts+=1
#     return counts
# print(find_length("Harsh"))
"Check sorted list"
"Ascending order"
# def is_sorted_ascending(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#     return True

# nums = [1, 2, 3, 4, 5]
# print(is_sorted_ascending(nums))
"Find GCD of two numbers"
# def find_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# print(find_gcd(50,10))




    



