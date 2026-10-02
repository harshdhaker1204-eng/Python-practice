"pratice question no 1"
# class BankAccount:
#     def __init__(self,name,Acc_no,balance):
#         self.name=name
#         self.Acc_no=Acc_no
#         self.__balance=balance
#     def user_details(self):
#         print("customer name", self.name)
#         print("Customer Acc_no", self.Acc_no)
#     def deposit(self):
#         amount = int(input("Enter Amount to deposit"))
#         self.__balance += amount
#         print("now Your Bank balance  is", self.__balance,"$")
#     def withdraw(self):
#         amount_W = int(input("Enter amount to withdraw"))
#         if self.__balance - amount_W < 500:
#             print("Balance must be more than 500")
#         else:
#             self.__balance -= amount_W
#             print("now your bank balance is", self.__balance,"$")
#     def get_balance(self):
#         return self.__balance
# B1=BankAccount("vedant jain","0808IO231023",100000)
# B1.user_details()

# # A=B1.get_balance()
# # print("Customer bank balance",A)
# B1.deposit()
# B1.withdraw()

"Pratice question no 2"
# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def set_marks(self):
#         if 100>=self.__marks>=90:
#             print("Grade A")
#         elif 89>=self.__marks>=75:
#             print("Grade B")
#         elif 74>=self.__marks>=50:
#             print("Grade C")
#         else:
#             print("Fail")
#     def display(self):
#         return self.__marks
# S1=Student(73)
# # S1.display()
# S1.set_marks()

"Pratice question no 3"
# class Employee:
#     def __init__(self):
       
#         self.__salary=0
#     def set_salary(self,salary):
#         if salary < 0:
#             print("Salary cannot be zero")
#         else:
#             self.__salary=salary
#     def get_salary(self):
#         return self.__salary
# E1=Employee()
# # E1.set_salary(1000000)
# # print("Employee Salary",E1.get_salary())

# E1.set_salary(-1000)
# print("Employee Salary",E1.get_salary())

"Pratice question no 4"
# class Mobile:
#     def __init__(self,password):
#         self.__password=password
#     def change_password(self,old_password,new_password):
#         if self.__password==old_password:
#             self.__password=new_password
#             print("Password change successfully")
#         else:
#             print("Wrong old password")
#     def Verify_password(self,password):
#         if password==self.__password:
#             print("Correct password ")
#         else :
#             print("Wrong password")
# M=Mobile("1234")
# M.Verify_password("1234")
# M.change_password("1234","4321")
# M.Verify_password("4321")

"Pratice question no 5"
# class ATM:
#     def __init__(self,pin,balance):
#         self.__pin=pin
#         self.__balance=balance
#     def set_pin(self,old_pin,new_pin):
#         if old_pin==self.__pin:
#             self.__pin==new_pin
#             print("ATM pin change successfully")
#         else:
#             print("Enter wrong pin")
#     def deposit(self):
#         amount = int(input("Enter Amount to deposit"))
#         self.__balance += amount
#         print("now Your Bank balance  is", self.__balance,"$")
#     def withdraw(self):
#         amount_W = int(input("Enter amount to withdraw"))
#         if self.__balance - amount_W < 500:
#             print("Balance must be more than 500")
#         else:
#             self.__balance -= amount_W
#             print("now your bank balance is", self.__balance,"$")
# A=ATM("1234",10000)
# A.set_pin("1234","4321")
# A.deposit()
# A.withdraw()

"Pratice question no 6"
# class car:
#     def __init__(self,speed):
#         self.__speed=speed
#     def accelerate(self):
#         if self.__speed<=0:
#             print("Speed can not go below")
    
#     def brake(self):
#         if self.__speed==0:
#             print("Brake the car")
#     def show_speed(self):
#         print("Car speed",self.__speed)
# C=car(10)
# C.accelerate()
# C.brake()
# C.show_speed()

"Pratice question no 7"
# class Laptop:
#     def __init__(self,battery):
#         self.__battery=battery
#     def charge(self):
#         if self.__battery<=30:
#             print("Please charge your laptop")
#     def use_laptop(self,hours):
#         second=3600*hours
#         print(f"Laptop is used for { hours} hours")
#         print(f"Total Seconds {second} seconds")

#     def show_battery(self):
#         print("laptop battery",self.__battery)
# L=Laptop(50)
# L.charge()
# L.use_laptop(10)
# L.show_battery()

"Pratice question no 8"
# class MovieTicket:
#     def __init__(self,total_seats):
#         self.__seats=total_seats
#     def Book_tickets(self,number):
#         if number<=0:
#             print("Please Enter valid number ticket")
#         elif number>=self.__seats:
#             print("Not enough seat available")
#         else:
#             self.__seats-=number
#             print(number,"ticket successfully book")
#     def Cancel_tickets(self,number):
#         if number<=0:
#             print("Please Enter a valid number of tickets")
#         else:
#             self.__seats+=number
#             print(number,"Tickets cancel successfully")
#     def show_available_seats(self):
#         print("Total available seats",self.__seats)
# M=MovieTicket(120)
# M.Book_tickets(60)
# M.Cancel_tickets(20)
# M.show_available_seats()


"Pratice question no 9"
# class Wallet:
#     def __init__(self):
#         self.__money=0
#     def add_money(self,money):
#         self.__money=money
#     def purchase_item(self,item_price):
#         if self.__money<=100:
#             print("You cannot buy item you have not enough money to purchase product ")
#         else:
#             self.__money-=item_price
#             print("total purchase item cost",item_price)
#     def show_money(self):
#         print("Total money now you have ",self.__money)

# W=Wallet()
# W.add_money(100)
# W.purchase_item(10000)
# W.show_money()

"Pratice question no 10"
# class Temperature:
#     def __init__(self):
#         self.__celsius=0
#     def set_temperature(self,temp):
#         self.__celsius=temp
#     def get_fahrenheit(self):
#         Fahrenheit=(self.__celsius*9/5)+32
#         return Fahrenheit
# T=Temperature()
# T.set_temperature(20)
# print("Total Fahrenheit",T.get_fahrenheit())



        



        



        

        



        

            
        




    

        





        






        


        


        