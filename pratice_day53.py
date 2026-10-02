"Pratice question no 1"
# def cube(a):
#     return a*a*a
# print(cube(3))

"Pratice question no 2"
# def check_number(n):
#     if n%5==0:
#         return "Number is divisible by 5"
#     else:
#         return "Number is not divisible by 5"
# print(check_number(7))
# print(check_number(5))

"Pratice question no 3"
# def minimum_of_three_number(a,b,c):
#     if a>b and a>c:
#         return f"{a} is greater then {b} and { c}"
#     elif b>a and b>c:
#         return f"{b} is greater then {a} and { c}"
#     elif c>a and c>b:
#          return f"{c} is greater then {a} and { b}"
#     else:
#         return f"{a} and {b},{c} are equal "
# print(minimum_of_three_number(1,2,3))

"Pratice question no 4"
# def count_number_of_digit(n):
#     if n==0:
#         return 1
#     count=0
    
#     while n>0:
#         n=n//10
#         count+=1
        
#     return count
# print(count_number_of_digit(100))

"Pratice question no 5"
# def Celsius_to_Fahrenheit(celsius):
#     Fahrenheit=(celsius*1.8)+32
#     return Fahrenheit
# print(Celsius_to_Fahrenheit(10))

"Pratice question no 6"
# def gcd(a,b):
#     a=abs(a)
#     b=abs(b)

#     while b!=0:
#         a,b=b,a%b
#     return a
# num1=56
# num2=98
# result=gcd(num1,num2)
# print(f"GCD of {num1} and {num2} is {result}")

"Pratice question no 7"
# def merge_list(a,b):
#     return a+b
# print(merge_list([1,2,3],[4,5,6]))

"Pratice question no 8"
# def Armstrong_number(n):
#     temp=n
#     arm_strong=0
#     digits = len(str(n))
#     while temp>0:
#         digit=temp%10
#         arm_strong += digit ** digits
#         temp=temp//10
#     if n==arm_strong:
#         return f"{n} is armstrong number"
#     else:
#         return f"{n} is not armstrong number"
# print(Armstrong_number(153))

"Pratice question no 9"
# def count_frequency(n):
#     freq={}
#     for item in n:
#         if item in freq:
#             freq[item]+=1
#         else:
#             freq[item]=1
#     return freq
# n=[1,2,2,3,1,4,2]
# print(count_frequency(n))


"Pratice question no 10"
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n %i==0:
#             return False
#     return True
# def Prime_upto_n(n):
#     Primes=[]
#     for i in range(2,n+1):
#         if is_prime(i):
#             Primes.append(i)
#     return Primes

# print(Prime_upto_n(10101))

"Pratice question no 11"
# def sum_number(n):
#     sum=0
#     i=1
#     while i<=n:
#         sum+=i
#         i+=1
#     return sum
# print(sum_number(10))

"Pratice question no 12"
# def print_number(n):
#     if n==0:
#         return 
#     print_number(n-1)
#     print(n)

# print(print_number(5))

"Pratice question no 13"
# def count_digits(n):
#     if n==0:
#         return 0
#     return 1+count_digits(n//10)
# print(count_digits(1234))

"Pratice question no 14"
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# print(gcd(56,98))


















        









