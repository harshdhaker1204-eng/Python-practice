"Reverse a number"
# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)

"Check palindrome number or not"

# num=int(input("ENter a number"))
# original=num
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10

# if original==reverse:
#     print("Palindrome")
# else:
#     print("This not a palindrome ")


"Count vowels in strint"
# str=input("Enter a character")
# count=0
# vowels="aeiouAEIOU"

# for ch in str:
#     if ch in vowels:
#         count+=1
# print("The total vowels in character is",count)

"Sum of digits"
# num=55
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)

"Find Largest in list"

# number=[]

# for i in range(5):
#     num=int(input(f".Enr a numbe {i+1} "))
#     number.append(num)
# largest=number[0]

# for num in number:
#     if num>largest:
#         largest=num
# print("Largest number is:",largest)

"Fibonacci series"

# n = int(input("Enter position: "))

# first = 0
# second = 1

# if n == 0:
#     print("Fibonacci number:", 0)

# elif n == 1:
#     print("Fibonacci number:", 1)

# else:
#     for i in range(2, n+1):
#         next_num = first + second
#         first = second
#         second = next_num

#     print("Fibonacci number:", second)

"Factorial"

# fact=int(input("Enter a number"))
# result=1

# for i in range(1,fact+1):
#     result=result*i
# print("The factorial is",result)


"Count words in sentence"

# sen = input("Enter sentence: ")
# count = 0

# for i in range(len(sen)):
#     if sen[i] == " ":
#         count += 1

# print("The total number of words is", count + 1)
"remove duplicates from list"
# number=[]
# n=int(input("Enter a list"))

# for i in range(n):

#     num=int(input(f"Enter number{i+1}:"))
#     number.append(num)

# unique_list=[]
# for num in number:
#     if num not in unique_list:
#         unique_list.append(num)
# print("Original list:",number)
# print("List after removing",unique_list)

    
 













