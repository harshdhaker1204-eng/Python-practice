"pratice question no 1"
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# S1=student("ABC",20)
# print(S1.name)
# print(S1.age)

"pratice question no 2"
# class car:
#     def __init__(self,brand="mahindra",model="Scorpio"):
#         self.brand=brand
#         self.model=model

# c1=car()
# print(c1.brand)
# print(c1.model)

# c2=car("TATA","Nexon")
# print(c2.brand)
# print(c2.model)

"Pratice question no 3"
# class Employee:
#     def __init__(self,name):
#         self.name=name
# E1=Employee("Alok")
# print(E1.name)

"Pratice question no 4"
# class city:
#     def __init__(self,name):
#         self.name=name
# c1=city("Neemuch")
# print(c1.name)

"Pratice question no 5"
# class student:
#     def __init__(self,age):
#         self.age=age
# a1=student(20)
# print("before",a1.age)
# a1.age=25
# print("After",a1.age)

"Pratice question no 6"
# class laptop:
#     def __init__(self,name):
#         self.name=name
# n1=laptop("lenovo")
# print(n1.name)

# n1.name="HP"
# print(n1.name)

"Pratice question no 7"
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("A",20)
# print(p1.name)
# print(p1.age)

# del p1.age
# print(p1.age)
# print(p1.name)

# del p1.name
# print(p1.name)

"Pratice question no 8"
# class operator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         print( self.a+self.b)
#     def sub(self):
#         print( self .a- self.b)
#     def mul(self):
#         print(self.a*self.b)
#     def div(self):
#         print(self.a/self.b)
# o1=operator(10,10)
# # del o1.a
# o1.sum()
# o1.sub()
# o1.mul()
# o1.div()

# del o1.a
# o1.sum()
# o1.sub()
# o1.mul()
# o1.div()

"Pratice question no 9"
# class student:
#     school="ABC"
# p1=student()
# print(p1.school)


"Pratice question no 10"
# class student:
#     school="ABC"

#     def __init__(self,name):
#         self.name=name
# s1=student("Naitik")
        

# print(s1.name)
# print(s1.school)

"Pratice question no 11"
# class person:
#     lastname=""
#     def __init__(self,name):
#         self.name=name

# p1=person("alok")
# p2=person("vedant")

# person.lastname="Jain"

# print(p1.lastname)
# print(p2.lastname)

"Pratice question no 12"
# class student:
#     school="ABC"
# s1=student()
# s2=student()

# print("Before change")
# print(s1.school)
# print(s2.school)

# s1.school="XYZ"
# print("After change")
# print(s1.school)
# print(s2.school)

"Pratice question no 13"
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student("Rohit")

# s1.age=13
# s1.city="chittor"

# print(s1.name)
# print(s1.age)
# print(s1.city)

"Pratice question no 14"
# class student:
#     school =" ABC"
# s1=student()
# s2=student()

# s1.school="XYZ"

# print("s1",s1.school)
# print("s2",s2.school)

"Pratice question no 15"
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print( "The addition of two number",self.a+self.b)
    
# c1=calculator(1,1)
# c1.add()

"Pratice question no 16"
# class area:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area_of_rectangle(self):
#         print("The area of rectangle are",self.length*self.width)
# a1=area(10,5)
# a1.area_of_rectangle()

"Pratice question no 17"
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_inf(self):
#         print(f"{self.name} and {self.age} year old")
# p1=person("virat kohli",37)
# p1.get_inf()

"Pratice question no 18"
# class car:
#     def __init__(self,brand,price):
        
#         self.brand=brand
#         self.price=price

#     def get_price(self):
#         return self.price
# c1=car("BMW",50000000)
# print("car price",c1.get_price())

"Pratice question no 19"
# class person:
#     def __init__(self ,name,age):
#         self.name=name
#         self.age=age
#     def celebrate_birthday(self):
#         self.age+=1
#         print(f"Happy birthday champ ! now you are age now {self.age}")
# p1=person("Virat kohli",37)
# p1.celebrate_birthday()
# p1.celebrate_birthday()

"Pratice question no 20"
# class Back_account:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
    
#     def deposit(self):
#         money=int(input("you can deposit money in your bank account ="))
#         self.balance+=money
#         print("Now your bank balance is",self.balance)
# B1=Back_account("Aanandu",100)
# print(B1.name)
# B1.deposit()

"Pratice question no 21"
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f" {self.name} ({self.age})"
# s1=student("aman",23)
# print(s1)

"Pratice question no 22"
# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def __str__(self):
#         return f"Car name:{self.brand}, price:{self.price}"

# c1=car("BMW",5000000)
# print(c1)

"Pratice question no 23"
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def subtract(self):
#         return self.a-self.b
#     def multiplication(self):
#         return self.a * self.b
#     def division(self):
#         return self.a/self.b
# c1=calculator(100,50)
# print(c1.add())
# print(c1.subtract())
# print(c1.multiplication())
# print(c1.division())

"Pratice question no 24"
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self):
#         deposit_money=int(input("please deposit money"))
#         self.balance+=deposit_money
#         print("Now your bank balance is",self.balance)
#     def withdraw(self):
#         withdraw_money=int(input("Enter the amount of money you want to withdraw"))
#         if self.balance<0:
#             return "you does not have sufficient money "
#         self.balance-=withdraw_money
#         print("now your bank balance is",self.balance)
# B1=BankAccount("naitik",1000)
# print("Account holder name ",B1.name)
# B1.deposit()          
# B1.withdraw()

"Pratice question no 25"

# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print("Hello")
# p1=person("Emil")
# del person.greet
# p1.greet()

"Pratice question no 26"
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print("Hello")
# p1=student("Kanishk",21)

# del p1.age
# print(p1.name)





        



    
        


        

        
        






        

        





        
        


        



        


        





        










        





        


        


        


        


    
        




        


