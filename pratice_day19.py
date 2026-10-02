"Pratice question 1"
'''1️ Class & Object (Basic)
  Student naam ki class banao
  Attributes: name, roll_no
  Method: display() jo student details print kare'''
# class Student():
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display(self):
#         print("Student name is", self.name)
#         print("Student roll number is", self.roll_no)

# S = Student("Harsh", 12345)
# S.display()

'''Constructor (__init__)
 Employee class banao
 Attributes: emp_id, salary
 Constructor ke through values pass karo
 Method: show_details()'''
# class Employee():
#     def __init__(self,em_id,salary):
#         self.em_id=em_id
#         self.salary=salary
#     def show_details(self):
#         print("Employee is is",self.em_id)
#         print("Employee salary is",self.salary,"$ per month")
# E1=Employee(1234,40000)
# E1.show_details()
''' Instance vs Class Variable
    Mobile class banao
    Class variable: brand = "Samsung"
    Instance variable: price
    objects banao aur difference print karo'''

# class Mobile():
#     brand="Samsung"
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price

#     def show(self):
#         print(self.model,"-",self.price,"-",Mobile.brand)
    
# m1=Mobile("Samsung F23",27000)
# m2=Mobile("Samsung S23",20000)

# m1.show()
# m2.show()

# if m1.price>m2.price:
#     print("samsung F23 is expensive")
# else:
#     print("Samsung S23 is expensive")
        
''' Encapsulation
BankAccount class banao
Private variable: __balance
Methods:
deposit(amount)
withdraw(amount)
get_balance()'''

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance
# B = BankAccount(2000)

# B.deposit(500)
# B.withdraw(300)
# print("Available Balance:", B.get_balance())
''' Single Inheritance
    Vehicle class
    Method: start()
    Bike class
    Vehicle se inherit karo
    start() call karo'''

# class Vehicle():
#     def start(self):
#         print("Vehicle start successfuly")
# class Bike(Vehicle):
#     pass
# B=Bike()
# B.start()
''' Method Overriding
    Animals class
    Method: sound()
    Dog aur Cat class
    sound() method override karo'''
# class Animals:
#     def sound(self):
#         print("Animals make sound")

# class Dog(Animals):
#     def sound(self):
#         print("Bhoo-Bhoo")

# class Cat(Animals):
#     def sound(self):
#         print("Meow-Meow")

      
# A = Animals()
# D = Dog()
# C = Cat()

# A.sound()
# D.sound()
# C.sound()
'''Multiple Inheritance
   Teacher class → teach()
   Researcher class → research()
   Professor class jo dono inherit kare'''

# class Teacher():
#     def teach(self):
#         print("Teacher teach the class")
# class Research():
#     def Researcher(self):
#         print("Researcher search new things")
# class Professor(Teacher,Research):
#     def pro(self):
#         print("Professor sometimes teach the class and rearcher new things")
# T=Teacher()
# R=Research()
# P=Professor()

# T.teach()
# R.Researcher()
# P.pro()






        



        


