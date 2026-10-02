"Pratice question no 1"
# num=int(input("Enter a number"))
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")

"Pratice question no 2"
# num=int(input("Enter a number"))

# print("The square is",num*num)
# print("The cube is",num*num*num)


"Pratice question no 3"
# a=1
# b=2
# c=3

# if a>b>c:
#     print("a is greater then to b and c")
# elif b>a>c:
#     print("b is greater then to a and c")
# else:
#     print("c is greater then to a and b")

"Pratice question no 4"
# S="Python"
# R=S[::-1]
# print("The reverse string is",S)

"Pratice question no 5"
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")











