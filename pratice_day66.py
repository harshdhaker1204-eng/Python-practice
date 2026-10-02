"Pratice question no 1"
# def add_number(a,b,c,d):
#     return a+b+c+d
# number=[4,3,2,1]
# print(add_number(*number))

"Pratice question no 2"
# def add_number(*number):
#     return number
# print(add_number(1,2,3,4,5,6,7,8,9,10))

"Pratice question no 3"
# def max_num(*num):
#     return max(num)
# print(max_num(1,2,3,4,5,6,7,8,9,10,11))

"Pratice question no 4"
# def max_num(*numbers):
#     max_num=numbers[0]
#     for num in numbers:
#         if num>max_num:
#             max_num=num
#     return max_num
# print(max_num(1,2,3,4,5,6,7,8,9,10,11))

"Pratice question no 5"
# def count_even(*numbers):
#     count=0
#     for num in numbers:
#         if num%2==0:
#             count+=1
#     return count
# print(count_even(1,2,3,4,5,6,7,8,9,10))

"Pratice question no 6"
# def reverse_string(*n):
#     for word in n:
#         reversed_txt= ""
#         for cha in word:
#            reversed_txt = cha + reversed_txt
#         print(reversed_txt,end=" ")
# reverse_string("Dog","Cat")

"Pratice question no 6"
# def reverse_string(str1):
#     return str1[::-1]
# l1=["Cat","Dog"]
# for word in l1:
#     print(reverse_string(word),end=" ")


"Pratice question no 7"
# def student_info(**student_detail):
#     return student_detail
# print(student_info(name="Harsh",age=21,branch="CSE"))

"Pratice question no 8"
# def bill(*items):
#     items={"Mobile":12000,"Charger":500,"cover":200}
#     product=0
#     for i in items.values():
#         product+=i
#     print(product)
# bill()


"Practice question no 8"

# def longest_value(**value):
#     longest = max(value.values(), key=len)
#     print(longest)

# longest_value(
#     City="Delhi",
#     country="India",
#     College="Engineering"
# )

"Practice question no 9"
# def mixed_fun(*x,**y):
#     return x,y
# print(mixed_fun("Harsh","Python","DSA",age=21,city="Indore"))

"Pratice question no 10"
# def shopping_cart(*args,**kwargs):
#     return args,kwargs
# print(shopping_cart(total_price="1200$",Customer_name="Vedant jain",address="Ap 4 boys hostel"))

"Pratice question no 11"
# x=10
# def test():
#     x=5
#     print(x)
# test() 
# print(x)

"Pratice question no 12"
count = 0

def increment():
    global count
    count += 1

increment()
print(count)






    

















