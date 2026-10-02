"pratice question 1"
"Ek class student banao jisme: atributes:name ,roll_no ,method:display() jo student details print kare"
# class Student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def display(self):
#         print("Student name",self.name)
#         print("Student roll_no",self.roll_no)
# s1=Student("Alok",1234)
# s1.display()
"Pratice question 2"
"Constuctor(__init__) employee class banao: 1) attributes id,salary 2)constructor se values set karo,3)show_details method banao"
# class Employee:
#     def __init__(self,id,salary):
#         self.id=id
#         self.salary=salary

#     def show_details(self):
#         print("Employee id",self.id)
#         print("Employee salary",self.salary,"$")

# s1=Employee(12345,40000)
# s1.show_details()

"pratice question 3"
"car class banao 1) attributes: brand,speed.2) method increase_speed(value) jp speed badhaye"
# class car:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
    
#     def increase_speed(self,value):
#         self.speed+=value
#         print("Brand is",self.brand)
#         print("Speed is",self.speed,"km per hour")

# c1=car("odi",200)
# c1.increase_speed(30)
"pratice question 4"
"college class banao: 1) class variable:college_name,2) instance variables:student_name,branch,3) sabka data print karo"
"pratice question 4"
"college class banao: 1) class variable:college_name,2) instance variables:student_name,branch,3) sabka data print karo"
# class college:
#     college_name="IPS academy indore"
#     def __init__(self,student_name,branch):
#         self.student_name=student_name
#         self.branch=branch
#     def show_details(self):
#         print("student name ",self.student_name)
#         print("Student branch",self.branch)
    
# s1=college("aman kumar","FT")
# s2=college("Alok tripathi","Civil")
# s3=college("Vedant jain","CS")
# s4=college("Rudra rathore","Civil")

# s1.show_details()
# s2.show_details()
# s3.show_details()
# s4.show_details()

"pratice question 5"
"inheritance(single) 1) animal class banao,2)method sound() 3) dog class banao jo animal se inherit kare 4) sound method override karo"
# class Animals:
#     def sound(self):
#         print("Animals make sound")
# class Dog(Animals):
#     def sound(self):
#         print("Bark...bark")
# a=Animals()
# b=Dog()
# a.sound()
# b.sound()
"Pratice question 6"
"Father class-skills(),mother class-skills() child class dono se inherit kare aur skills print kare"

# class Father:
#     def skills(self):
#         print("Father skills :best learner")
# class Mother:
#     def skills(self):
#         print("Mother skills :best sports player")
# class child(Father,Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("Child skills: Intelligent and Active")
# F=Father()       
# M=Mother()
# c=child()
# F.skills()
# M.skills()
# c.skills()
# Parent class

"Pratice question 7"
# class Bank:
#     def rate_of_interest(self):
#         return 4   # default interest rate

# # Child class
# class SBI(Bank):
#     def rate_of_interest(self):
#         return 6.5   # SBI ka apna interest rate

# # object creation
# b = Bank()
# s = SBI()

# print("Bank Interest Rate:", b.rate_of_interest(), "%")
# print("SBI Interest Rate:", s.rate_of_interest(), "%")

"Pratice question 8"
# class Account:
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposited:",amount)
#     def withdraw(self,amount):
#         if amount <=self.__balance:
#             print("Withdraw",amount)
#         else:
#             print("Insufficient balance")
#     def show_balance(self):
#         print("Balance:",self.__balance)
# acc=Account(1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.show_balance()

"Pratice question 9"
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return  3.14*self.radius*self.radius
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
    
# c=Circle(5)
# r=Rectangle(4,6)
# print("Circle ARea",c.area())
# print("Rectangle Area",r.area())
"Pratice question 10"
# class library:
#     def __init__(self):
#         self.books=[]
#     def add_book(self,book):
#         self.books.append(book)
#         print(book,"added successfully")
#     def remove_book(self,book):
#         if book in self.books:
#             self.books.remove(book)
#             print(book,"Removed successfully")
#         else:print("Book not found")
#     def show_books(self):
#         if not self.books:
#             print("No books available")
#         else:
#             print("Available books:")
#             for book in self.books:
#                 print("-",book)
# lib=library()
# lib.add_book("Python Basics")
# lib.add_book("Data Structures")
# lib.show_books()
# lib.remove_book("Python Basics")
# lib.show_books()
        

        
        




        

    
    
    


       
        




     



        
        
        
        

        




        
        