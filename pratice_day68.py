"pratice question no 1"
# x=lambda a:a**2
# print("Output",x(10))

"pratice question no 2"
# x=lambda a: print("Even") if a%2==0 else print("odd")
# print("Even or odd",x(10))

"pratice question no 3"
# numbers=[1,2,3,4,5,6]
# doubled=list(map(lambda x:x*2,numbers))
# print(doubled)

"pratice question no 4"
# student=[("Vedant pitaliya",21),("Aryan dangi",22),("naitik thakur",23)]

# # students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_student=sorted(student,key=lambda x:x[1])
# print(sorted_student)



# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x:x[1])
# print(sorted_students)

"pratice question no 5"

# numbers=[-1,2,3,-4,5,6,8,-9]
# positive_no=list(filter(lambda x:x>0,numbers))
# print(positive_no)
"pratice question no 6"
# numbers=[-1,2,3,-4,5,6,8,-9]
# max_no=max(numbers,key=lambda x:x)
# print(max_no)

"pratice question no 7"
# from functools import reduce
# numbers=[1,2,3,4,5]
# product=reduce(lambda x,y :x*y,numbers)
# print(f"Product of all numbers {product}")

"pratice question no 8"
# names=["vijay","Sonu","Vikas"]
# upper_case=lambda x:x.upper()
# result = list(map(upper_case, names))

# print(result)

"pratice question no 9"

# x=lambda x:len(x)
# print("Length",x("Teri maa ki "))

"pratice question no 10"
# numbers=[66,45,55,60,80,90]
# result = list(map(lambda x: "Pass" if x >= 40 else "Fail", numbers))
# print(result)

"pratice question no 11"
# my_dict={"apple":5,"banana":3,"cherry":10}

# sorted_my_dict = dict(sorted(my_dict.items(), key=lambda item:item[1]))
# print(sorted_my_dict)

"pratice question no 12"
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

"pratice question no 13"
# def sum_natural_no(n):
#     if n<=0:
#         return 0
#     if n==1:
#         return 1
    
#     return n+sum_natural_no(n-1)
# print(sum_natural_no(10))  
# 
"pratice question no 14"
# def print_n_no(n):
#     if n==0:
#         return
#     print_n_no(n-1)
#     print(n,end=" ")
# print_n_no(10)

"pratice question no 15"

# def print_n_no(n):
#     if n == 0:
#         return
    
#     print(n,end=" ")
#     print_n_no(n - 1)

# print_n_no(10)

"pratice question no 16"
# def fib(n):
#     if n==0 :
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(8))

"pratice question no 17"
# def reverse(n):
#     if n=="":
#         return
#     print(n[-1],end="")
#     reverse(n[:-1])
# reverse("Hello")

"pratice question no 18"


# def count_digits(n):
#     n=abs(n)
#     if n<10:
#         return 1
#     return 1+count_digits(n//10)
# print(count_digits(12344))

"pratice question no 19"
# def power(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*power(a,b-1)
# base=2
# exponent=3
# result=power(base,exponent)
# print(f"{base}^{exponent}={result}")


"pratice question no 20"
# def sum_of_digits(n):
#     sum=n%10
#     if n<10:
#         return 1
   
#     return sum+sum_of_digits(n//10)
# print(sum_of_digits(1234))


















