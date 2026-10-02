"Pratice question no 1"
# def is_prime(n,i=2):
#     #Base cases
#     if n<=1:
#         return False
#     if i*i>n:
#         return True
#     if n%i==0:
#         return False
#     return is_prime(n,i+1)
# def print_primes(start,end):
#     #Base case
#     if start >end:
#         return
#     if is_prime(start):
#         print(start)
#     print_primes(start+1,end)
# print_primes(1,20)


"Pratice question no 2"
# def fibo(n):

#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibo(n-1) + fibo(n-2)


# nums = []

# for i in range(20):
#     nums.append(fibo(i))

# print(nums)

"Pratice question no 3"

# def Frequency_counter(text):
#     count=0
#     for _ in text:
#         count+=1
#     print(count)
# Frequency_counter("Hello")

"Pratice question no 4"
# def second_largest(nums):
#     nums.sort()
    
#     return nums[-2]

  
# print(second_largest([9,8,7,6,5,4,3,2,1]))

"Pratice question no 5"
# def remove_duplicates(n):
#     my_set=set(n)
#     return my_set
   
# print(remove_duplicates([1,1,1,2,2,3,3,4,4,5,5,6,6]))

"Pratice question no 6"
# def palindrome_checker(n):
#     temp=n
#     if n==temp[::-1]:
#         print("Palindrome ")
#     else:
#         print("Its not a Palindrome")
# palindrome_checker("madam")

"Pratice question no 7"
# def count_V_C(n):
#     vowels="aeiouAEIOU"
#     count_vowels=0
#     count_Consonants=0

#     for char in n:
#         if char.isalpha():
#            if char in vowels:
#               count_vowels+=1
              
#            else :
#                count_Consonants+=1
               
#     print("Vowels count",count_vowels)
#     print("Count consonants",count_Consonants)
# count_V_C("Hello my name is optimus prime")

"Pratice question no 8"
# def matrix_addition(mat1,mat2):
#     result=[]
#     for i in range(len(mat1)):
#         row=[]
#         for j in range(len(mat2[0])):
#             row.append(mat1[i][j] + mat2[i][j])
#         result.append(row)
#     return result
# mat1=[[1,2],
#       [3,4]]
# mat2=[[5,6],
#       [7,8]]
# print(matrix_addition(mat1,mat2))

"Pratice question no 9"
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

"Pratice question no 10"
# def sort_dict(data):
#     sorted_values=sorted(data.values())
#     return sorted_values

    
# print(sort_dict({'apple': 3,
#     'banana': 1,
#     'cherry': 5,
#     'date': 2}))

"Pratice question no 11"
# def most_frequent(nums):
#     freq={}
#     for i in nums:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return max(freq,key=freq.get)
# print(most_frequent([1,2,2,3,3,3,4,4,4,4,5]))

"Pratice question no 12"
# def compress_string(s):
#     compressed=""
#     count=1

#     for i in range(len(s)):
#         #count repeated characters
#         if i<len(s)-1 and s[i]==s[i+1]:
#             count+=1
#         else:
#             compressed+=s[i]+str(count)
#             count=1
#     return compressed
# print(compress_string("aaabbc"))
# print(compress_string("wwwwaaadex"))

"Pratice question no 13"
# def merge_dict(d1,d2):
#     d3={}
#     for key in d1:
#         d3[key]=d1[key]
#     #Merge second dictionary
#     for key in d2:
#         if key in d3:
#             d3[key]+=d2[key]
#         else:
#             d3[key]=d2[key]
#     return d3
# d1={"apple":4,"banana":12,"cherry":4,"Orange":10}
# d2={"apple":5,"banana":24,"cherry":5,"Watermelon":1}
  
# print(merge_dict(d1,d2))


"Pratice question no 14"
# def Armstrong_number(n):
#     temp=n
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit**3
#         temp//=10
#     if sum==n:
#        print("Armstrong number")
#     else:
#         print("Its not a Armstrong number")
# Armstrong_number(153)


"Pratice question no 15"
# def rotate_list(lst,k):
#     k=k%len(lst)
#     #Rotate list
#     rotate_list=lst[-k:]+lst[:-k]
#     return rotate_list
# nums=[1,2,3,4,5]
# print(rotate_list(nums,2))

"Pratice question no 16"
# def count_words(words):
#     word_list = words.split()  
#     count=0
#     for _ in word_list:
#         count+=1
#     return count
# print(count_words("Hello my name is optimus prime "))

"Pratice question no 17"
# def anagram_checker(s1,s2):
#     s1=s1.replace(" "," ").lower()
#     s2=s2.replace(" "," ").lower()
#     # Compare Sorted characters
#     if sorted(s1)==sorted(s2):
#         return "Anagram"
#     else:
#         return "Not Anagram"
# print(anagram_checker("Listen","Silent"))
# print(anagram_checker("Heart","earth"))
# print(anagram_checker("Hello","World"))

"Pratice question no 18"
# def common_elements(lst1,lst2):
#     s1=set(lst1)
#     s2=set(lst2)

    
#     return s1.intersection(s2)
# print(common_elements([2,3,4,5,1],[3,5,4,2,2,1]))

"Pratice question no 19"
# def decimal_to_binary(n):
#     if n==0:
#         return "0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
#     binary=""
#     while n>0:
#         remainder=n%2
#         binary=str(remainder)+binary
#         n//=2
#     return binary
# print(decimal_to_binary(10))

"Pratice question no 20"
# def check_password_strength(password):
#     special_chars="!@#$%^*()_+-=[]{}|;:,.<>?/"
#     #Rule 1:minimum length
#     if len(password)<8:
#         return "Weak Password :Minimum 8 characters required"
#     #Rule 2 :one uppercase
#     has_upper=False
#     # Rule 3: one lowercase
#     has_lower=False

#     # Rule 4:one digit
#     has_digit=False

#     # Rule5 :one special character

#     has_special=False

#     #checking each character
#     for ch in password:
#         if ch.isupper():
#             has_upper=True
#         elif ch.islower():
#             has_lower=True
#         elif ch.isdigit():
#             has_digit=True
#         elif ch in special_chars:
#             has_special=True
#     #Final checking
#     if has_upper and has_lower and has_digit and has_special:
#         return "Strong password"
#     else:
#         return "weak password"
# print(check_password_strength("Harsh@123"))
# print(check_password_strength("hello123"))

"Pratice question no 20"
# def nested_sum(lst):
#     total=0
#     for item in lst:
#         #if item is a list call function
#         if isinstance(item,list):
#             total+=nested_sum(item)
#         else:
#             total+=item
#     return total
# print(nested_sum([1,2,[3,4],[5,[6,7],8]]))

















    













    







        
