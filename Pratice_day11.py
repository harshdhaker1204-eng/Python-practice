"Check whether a number is a palindrome or not usinh a loop"
# num=int(input("Enter a number"))
# temp=num

# rev=0
# for _ in range (len(str(num))):
#     digit=temp%10
#     rev=rev*10+digit
#     temp//=10
# if num==rev:
#     print("Its a palindrome")
# else:print("Its not a palindrome")
"while loop"
# num=int(input("Enter a number"))
# rev=0
# original=num
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# if original==rev:
#     print("its palindrome")
# else:
#     print("Its not a palindrome")

"Find the largest digit in a number using a loop."
# num=input("Enter a number")
# largest=0
# for ch in num:
#     digit=int(ch)
#     if digit>largest:
#         largest=digit
# print("Largest number is",largest)
"While loop"
# num=int(input("Enter a number"))
# largest=0
# while num>0:
#     digit=num%10
#     if digit>largest:
#         largest=digit
#     num//=10
# print("Largest number is",largest)
"find the smallest digit in number using a loop"
# num=input("Enter a number")
# smallest=9
# for ch in num:
#     digit=int(ch)
#     if digit<smallest:
#         smallest=digit
# print("Smallest number is",smallest)
"Using while loop"
# num=int(input("Enter a number"))
# smallest=9
# while num>0:
#     digit=num%10
#     if digit<smallest:
#         smallest=digit
#     num//=10
# print("Smallest number are",smallest)
"print 1 to 200 print number"
# primes = []
# count = 0
# num = 2

# while count < 200:
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         primes.append(num)
#         count += 1

#     num += 1

# print(primes)
# num=int(input("Enter a number"))
# fact=1
# i=1
# while num>=i:
#    fact*=i
#    i+=1
# print(fact)

"factorial using function"

def fact(num):
    
    i=1
    fact=1
    while i<=num:
        fact*=i
        i+=1
    return fact
print(fact(5))
print(fact(6))

"Check Even or odd"
def Even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(Even_or_odd(2))
print(Even_or_odd(3))

"Count Vowels in string"
def count_vowels(s):
    vowels="aieouAIEOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
print(count_vowels("Harsh"))     # 1
print(count_vowels("aaaaaee"))   # 7

"Largest number in list"
def largest_number(num):
    largest=0
    while num>0:
        digit=num%10
        if digit>largest:
            largest=digit
        num//=10
    return largest
print(largest_number(123))
print(largest_number(100))

        
"Check prime number or not"
def is_prime_number(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime_number(1))
print(is_prime_number(2))
print(is_prime_number(3))
print(is_prime_number(4))
print(is_prime_number(5))
print(is_prime_number(6))
print(is_prime_number(7))
print(is_prime_number(8))
print(is_prime_number(9))













