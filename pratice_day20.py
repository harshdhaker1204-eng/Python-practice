"Pratice Question 1"
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_details(self):
#         print("The student name is",self.name)
#         print("Student age is",self.age)
# class Student(Person):
#     def __init__(self,roll_no):
#         self.roll_no=roll_no
#     def show_Student(self):
#         print("Student roll is ",self.roll_no)
# P=Person("Vedant jain",20)
# P.show_details()
# S=Student(1234567)
# S.show_Student()

"Pratice Questiion 2"

# class Animals():
#     def Sound(self):
#         print("Animals make sound")
# class Dog(Animals):
#     def Sound(self):
#         print("Bhoo-Bhoo")
# class Cat(Animals):
#     def Sound(self):
#         print("Moew-Moew")
# A=Animals()
# D=Dog()
# C=Cat()
# A.Sound()
# D.Sound()
# C.Sound()

"Pratice question 3"
# class Father():
#     def skill(self):
#         print("learner")

# class Mother():
#     def skill(self):
#         print("dancer")

# class child(Mother,Father):
#     def skill(self):
#         print("both")
# F=Father()
# M=Mother()
# c=child()
# F.skill()
# M.skill()
# c.skill()

"Pratice question 4"
# class Vehicle():
#     def start(self):
#         print("Veicle start")
# class Car(Vehicle):
#     def start(self):
#         print("Car start successfully")
# class Electric_Car(Car):
#     def battery_status(self):
#         print("90 '%' battery ")
# V=Vehicle()
# C=Car()
# E=Electric_Car()
# V.start()
# C.start()
# E.battery_status()

"Pratice question 5"
# class Employee():
#     def __init__(self ,name ,salary):
#         self.name=name
#         self.salary=salary

#     def show_employee(self):
#         print("Employee name:",self.name)
#         print("Salary:",self.salary)
# class Manager(Employee):
#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department=department
#     def show_manager(self):
#         self.show_employee()
#         print("Department:",self.department)
    
# m=Manager("ANnil",50000,"IT")
# m.show_manager

"Pratice question 6"

# class Account:
#     def Account_type(self):
#         print("My account is saving")

# class Saving_Account(Account):
#     def Account_S(self):
#         print("Saving account")

# class Current_Account(Account):
#     def Account_C(self):
#         print("Current account")

# A = Account()
# S = Saving_Account()
# C = Current_Account()

# A.Account_type()
# S.Account_S()
# C.Account_C()

"Pratice Question 7"
# class Teacher():
#     def details(self):
#         print("All are good teacher")
# class Math_Teacher(Teacher):
#       def __init__(self,name,age):
#            super().__init__()
#            self.name=name
#            self.age=age
#       def details(self):
#            print("Maths teacher name",self.name)
#            print("Maths teacher age",self.age)

# T=Teacher()
# M=Math_Teacher("Om",40)
# T.details()
# M.details()
"pratice question 8"
# class Bank:
#     def __init__(self, balance, account_no):
#         self.account_no = account_no
#         self.__balance = balance   # private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited money:", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdraw:", amount)
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print("Current balance:", self.__balance)


# class Customer(Bank):
#     def __init__(self, name, age, balance, account_no):
#         super().__init__(balance, account_no)  # Bank constructor call
#         self.name = name
#         self.age = age
# c1 = Customer("Harsh", 21, 5000, 12345)

# c1.deposit(2000)
# c1.withdraw(3000)
# c1.show_balance()
"Pratice question 9"
# class Device:
#     def __init__(self, brand_name):
#         self.brand_name = brand_name

#     def details(self):
#         print("Brand name is:", self.brand_name)


# class Mobile(Device):
#     def __init__(self, brand_name, model, ram):
#         super().__init__(brand_name)   # Parent constructor
#         self.model = model
#         self.ram = ram

#     def details(self):   # Method overriding
#         print("Brand name is:", self.brand_name)
#         print("Model name is:", self.model)
#         print("Device RAM is:", self.ram)
# D = Device("Samsung")
# D.details()

# print("-------------")

# M = Mobile("Samsung", "F23", "6GB")
# M.details()


   


     
        
        

        




        


        
