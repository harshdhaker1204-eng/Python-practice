"Pratice question no 1"
# class Car:
#     def __init__(self,car_name):
#         self.car_name=car_name
#     class Engine:
#         def __init__(self,car,Engine_A):
#             self.car=car
#             self.Engine_A=Engine_A
#         def display(self):
#             print(f"car name {self.car.car_name}")
#             print(f"Horsepower {self.Engine_A}")
# car=Car("BMW")
# engine=car.Engine(car,"320HP")
# engine.display()

"Pratice question no 2"
# class University:
#     def __init__(self,University_name):
#         self.University_name=University_name
#     class Department:
#         def __init__(self,UV,Department_name,HOD_name):
#             self.UV=UV
#             self.Department_name=Department_name
#             self.HOD_name=HOD_name
#         def display(self):
#             print(f"University name {self.UV.University_name}")
#             print(f"Department name {self.Department_name}")
#             print(f"HOD Name",{self.HOD_name})
# U=University("RGPV")
# D=U.Department(U,"CSE","Angeeta Hirwe")
# D.display()

"Pratice question no 3"
# class Computer:
#     def __init__(self,Computer_brand):
#         self.Computer_brand=Computer_brand
#     class Processor:
#         def __init__(self,CB,Processor_type,Number_of_Cores):
#             self.CB=CB
#             self.Processor_type=Processor_type
#             self.Number_of_Cores=Number_of_Cores
#         def show(self):
#             print(f"Computer brand {self.CB.Computer_brand}")
#             print(f"processor type {self.Processor_type}")
#             print(f"Number of cores {self.Number_of_Cores}")

# C=Computer("AMD,Intel")            
# P=C.Processor(C,"Ryzen 5","6 Cores")
# P.show()

"Pratice question no 4"
# class Mobile:
#     def __init__(self,Mobile_brand):
#         self.Mobile_brand=Mobile_brand
#     class Battery:
#         def __init__(self, M,BC,BP):
#             self.M=M
#             self.BC=BC
#             self.BP=BP
#         def show(self):
#             print(f"Mobile Brand {self.M.Mobile_brand}")
#             print(f"Battery capacity {self.BC}")
#             print(f"Battery Percentage {self.BP}")
# M1=Mobile("SAMSUNG")      
# B=M1.Battery(M1,"Good capacity","95%")
# B.show()

"Pratice question no 5"
# class School:
#     def __init__(self,School_name):
#         self.School_name=School_name
#     class Student:
#         def __init__(self,S_N,Student_name,Roll_no):
#             self.S_N=S_N
#             self.Student_name=Student_name
#             self.Roll_no=Roll_no
#         def Show_all_details(self):
#             print(f"School Name :{self.S_N.School_name}")
#             print(f"Student Name: {self.Student_name}")
#             print(f"Roll Number :{self.Roll_no}")
# S1=School("Divine Public School")
# Stu1=S1.Student(S1,"Vedant jain","0808AI231030")
# Stu1.Show_all_details()

"Pratice question no 6"
# class Bank:
#     def __init__(self):
#         self.Bank_name="SBI"
#     class Account:
#         def __init__(self,User_name,Balance):
            
#             self.User_name=User_name
#             self.Balance=Balance
#         def Deposit_method(self):
#             amount=int(input("Enter your amount to deposit"))
#             amount+=self.Balance
#             print("Your money has been successfully deposited in your back account thank you",amount)
#         def withdraw(self):
#             withdraw_money=int(input("Enter your to withdraw"))
#             withdraw_money-=self.Balance
#             if withdraw_money>self.Balance:
#                 print("You can't withdraw money your amount is more then your balance",withdraw_money)
#             else:
#                 print("Your money has been successfully withdraw thank you")
#         def show_balance(self):
#             print(f"user name {self.User_name}")
#             print("Your bank balance is",self.withdraw,"$")
# B=Bank()           
# print(B.Bank_name)
# A=B.Account("Vedant jain",10000)
# A.Deposit_method()
# A.withdraw()
# A.show_balance()

"Pratice question no 7"
# class Laptop:
#     def __init__(self):
#         self.name="Lenovo"
#     class Keyboard:
#         def __init__(self,Keyboard_Type,Backlight_Status):
#             self.Keyboard_Type=Keyboard_Type
#             self.Backlight_Status=Backlight_Status
#         def Back_light(self):
#             if self.Backlight_Status==1:
#                 print("True")
#             elif self.Backlight_Status==0:
#                 print("False")
#         def Display_information(self):
#             print(f"Keyboard Type {self.Keyboard_Type}")
# L=Laptop()
# print(L.name)
# K=L.Keyboard("BlueTooth",1)
# K.Back_light()
# K.Display_information()

"Pratice question no 8"
# class Hospital:
#     def __init__(self):
#         self.Hospital_name="AIIMS_Delhi"
#     class Doctors:
#         def __init__(self,Doctor_name,specialization,Expreience):
#             self.Doctor_name=Doctor_name
#             self.specialization=specialization
#             self.Expreience=Expreience
#         def Show_All_Details(self):
#             print(f"Doctor name :{self.Doctor_name}")
#             print(f"Specialization : {self.specialization}")
#             print(f"Expreience : {self.Expreience}")
# H=Hospital()
# print(H.Hospital_name)
# D=H.Doctors("ALok Bhosde","sexologist","5 years")
# D.Show_All_Details()

"Pratice question no 9"

# class Company:
#     def __init__(self):
#         self.name="Alok private limited"
#     class Employee:
#         def __init__(self,Employee_name,Salary):
#             self.Employee_name=Employee_name
#             self.Salary=Salary
#         def Employee_details(self):
#             print(f"Employee name is {self.Employee_name}")
#             print(f"Employee salary is {self.Salary} $")
#         def increase_salary(self):
#             IS=self.Salary/10
#             self.Salary+=IS
#             print(f"Employee Salary increase by 10% {self.Salary} $")
# C=Company()
# print(C.name)
# E=C.Employee("Vedant jain",10000)
# E.Employee_details()
# E.increase_salary()

"Pratice question no 10"
# class Library:
#     def __init__(self):
#         self.name="Study_cafe"
#     class Book:
#         def __init__(self,Book_title,Author_name,price):
#             self.Book_title=Book_title
#             self.Author_name=Author_name
#             self.price=price
#         def display_book_details(self):
#             print(f"Book Title : {self.Book_title}")
#             print(f"Book Author : { self.Author_name}")
#             print(f"Book price : { self.price}")
# L1=Library()
# print(L1.name)
# B1=L1.Book("How to Control masterbution","Alok Tripathi" ,"1000$")
# B1.display_book_details()

"Pratice question no 11"
# class Shopping:
#     def __init__(self,Shopping_platform_name):
#         self.Shopping_platform_name=Shopping_platform_name
#     class Product:
#         def __init__(self,SV,Product_name,Product_price,product_Quantity):
#             self.SV=SV
#             self.Product_name=Product_name
#             self.Product_price=Product_price
#             self.product_Quantity=product_Quantity

#         def Total_price(self):
#             TP=self.Product_price*self.product_Quantity
#             print(f"Total price: {TP}")

#         def Display_method(self):
#             print(f"Shopping platform name :{self.SV.Shopping_platform_name}")
#             print(f"product name : {self.Product_name}")
#             print (f"Product price:{self.Product_price}")
#             print(f"Product Quantity:{self.product_Quantity}")

# S1=Shopping("Flipcart")
# P1=S1.Product(S1,"Book",100,2)
# P1.Display_method()



            

        



        
            



            
        
            



        


            

            





              
            
        


            
        


            
        

            

        


            
        


            
        