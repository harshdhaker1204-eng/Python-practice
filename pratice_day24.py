"Question no1 "
# class Student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def show_details(self):
#         print(" student name is",self.name)
#         print(" student roll number is",self.roll_no)
# S1=Student("Vedant jain",12083)
# S1.show_details()
"Question no 2"
# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

#     def show_details(self):
#         print("Car brand is ",self.brand)
#         print("Car model is",self.model)
#         print("Car price is",self .price)
# C1=Car("Mahindra"," Mahindra Scorpio","₹13.99 lakh ")
# C1.show_details()
"Question no 3"
# class Bankaccount:
#     def __init__(self,balance):
#         self._balance=balance
#     def deposite(self,amount):
#         if amount >0:
#             self._balance+=amount
#             print("Amount deposited successfully")
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self,amount):
#         if  amount <=self._balance:
#             self._balance-=amount
#             print("amount withdraw successfully")
#         else:
#             print("Insufficient balance")
#     def get_balance(self):
#         return self._balance
# account=Bankaccount(1000)
# account.deposite(500)
# account.withdraw(300)
# print("Current  Balance",account.get_balance())

"Pratice question no 4"
# class Person:
#     def __init__(self,name):
#         self.name=name
# class Employee(Person):
#     def __init__(self, name,salary):
#         self.name=name
#         self.salary=salary
    
#     def display_info(self):
#         print("Employee name is",self.name)
#         print("Employee salary is",self.salary)
# E1=Employee("Aman kumar",100000)
# E1.display_info()

"Pratice question no 5"
# class Animals:
#     def sound(self):
#         print("Animals make sound")
# class Dog(Animals):
#     def sound(self):
#         print("Dog barks")
# A1=Animals()
# D1=Dog()
# A1.sound()
# D1.sound()

"Pratice question no 6"
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius    
       
# class Rectangle:
#     def __init__(self,Length,width):
#         self.Lenght=Length
#         self.width=width
#     def area(self):
#         return self.Lenght*self.width
    
# C1=Circle(5)
# R1=Rectangle(5,5)
# print("The area of circle is",C1.area())
# print("The area of Rectangle is",R1.area())

"Pratice question no 7"
# from abc import ABC ,abstractmethod
# class Shape(ABC):
#     def area(self):
#         pass
# class Square:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# class Triangle:
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height

#     def area(self):
#         return 0.5*self.base*self.height
# S1=Square(4)
# T1=Triangle(4,4)
# print("Area of Square is",S1.area())
# print("Area of triangle is",T1.area())

"Dates"
import datetime

x=datetime.datetime.now()
print(x.strftime("%C"))

        
        
        
    


    
        


        
        

        

        

        