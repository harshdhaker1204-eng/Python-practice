"pratice question no 1"
# class person:
#     def __init__(self,name ,age):
#         self.name=name
#         self.age=age
#     def display_method(self):
#         print("Person name is ",self.name)
#         print("Person age is",self.age)
# class student(person):
#     def __init__(self,marks):
#         self.marks=marks
#     def marks_display(self):
#         print("Student marks is",self.marks)
# S1=student(99)
# # S1.display_method()
# S1.marks_display()


"pratice question no 2"

# class vehicle:
#     def start_method(self):
#         print("Vehicle is starting")
# class car:
#     def derive_method(self):
#         print("Car is deriving")
# v1=vehicle()
# c1=car()

# v1.start_method()
# c1.derive_method()

"pratice question no 3"
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show_method(self):
#         print("Employee name is",self.name)
#         print("Employee salary is",self.salary)
# class developer(Employee):
#     def __init__(self,name,salary, language):
#          Employee.__init__(self,name,salary)
#          self.language=language
#     def show_language(self):
#         print("Developer language is",self.language)
#         print("Developer name is",self.name)
#         print("Developer salary is",self.salary)
# # E1=Employee("Nitin Bedre",21)
# D1=developer("Alok",22222,"Python")
# # E1.show_method()
# D1.show_language()

"pratice question no 4"
# class Animals:
#     def sound(self):
#         print("Animals makes sound")
# class Dog:
#     def dog_sound(self):
#         print("dogs are Barking")
# A1=Animals()
# A1.sound()
# D1=Dog()
# D1.dog_sound()


"pratice question no 5"
# class parent:
#     def __init__(self):
#         print("Parent constructor called")
# class Child(parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor called")
# obj=Child()

"pratice question no 6"
# class A:
#     def MethodA(self):
#         print("Hello A")
# class B:
#     def MethodB(Self):
#         print("Hello B")
# class C(A,B):
#     def MethodC(self):
#         print("Hello C")
# C1=C()
# C1.MethodA()
# C1.MethodB()
# C1.MethodC()

"pratice question no 7"
# class Father:
#     def __init__(self,money):
#         self.money=money
#     def show_money(self):
#         print("Total money",self.money,"₹")
# class Mother:
#     def __init__(self,gold):
#         self.gold=gold
#     def show_gold(self):
#         print("Total gold in rupees",self.gold,"₹")

# class Child(Father, Mother):
#     def __init__(self, money, gold):
#         Father.__init__(self, money)
#         Mother.__init__(self, gold)
#     def total_money_and_gold(self):
#         total_money=self.money+self.gold
#         print("Total money and gold",total_money,"₹")

# C1=Child(10000000,10023223001)
# C1.show_gold()
# C1.show_money()
# C1.total_money_and_gold()

"pratice question no 8"
# class A:
#     def show(self):
#         print("Method From A")
# class B:
#     def show(self):
#         print("Method From B")
# class C(A,B):
#     def show(self):
#          print("Method from C override")
#          super().show()
# Obj=C()
# Obj.show()

# print(C.__mro__)

"pratice question no 9"
# class Teacher:
#     def study(self):
#         print("Teacher is Teaching in  class")
# class Researcher:
#     def Search(self):
#         print("Researcher is Searching in ML")
# class professor(Teacher,Researcher):
#     def __init__(self):
#         Teacher.__init__(self)
#         Researcher.__init__(self)
#     def combination(self):
#         print("Professor is person who work in both field teaching and Researching")
# p1=professor()
# p1.study()
# p1.Search()
# p1.combination()
"pratice question no 10"
# class A:
#     def methodA(self):
#         print("Hello A")
# class B(A):
#     def methodB(self):
#         print("Hello B")
# class C(B):
#     def methodC(self):
#         print("Hello C")
# C1=C()
# C1.methodA()
# C1.methodB()
# C1.methodC()

"pratice question no 11"
# class Grandparent:
#     def __init__(self,house):
#         self.house=house
# class parent(Grandparent):
#     def __init__(self, house,car):
#         super().__init__(house)
#         self.car=car
# class child(parent):
#     def __init__(self, house, car ,Bike):
#         super().__init__(house, car)
#         self.Bike=Bike
#     def show_details(self):
#         print("House",self.house)
#         print("Car",self.car)
#         print("Bike",self.Bike)
# C1=child("Villa","BMW","KTM")
# C1.show_details()

"pratice question no 12"
# class Grandparents:
#     def __init__(self):
#         print("Grandparent Constructor called")
# class parent(Grandparents):
#     def __init__(self):
#         super().__init__()
#         print("Parent constructor called")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor called")
# obj=child()
# print(obj)

"pratice question no 13"

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def vehicle_info(self):
#         print("Vehicle brand:", self.brand)


# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def model_name(self):
#         print("Model name:", self.model)


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity

#     def show_battery(self):
#         print("Battery capacity of electric car:",
#               self.battery_capacity, "KWH")


# Obj = ElectricCar("Tesla", "Model S", 100)

# Obj.show_battery()
# Obj.model_name()
# Obj.vehicle_info()

"pratice question no 14"
# class parents:
#     def __init__(self):
#         print("Hello son how are you")
# class child(parents):
#     def __init__(self):
#         super().__init__()
#         print("YOO dad i am good")
# Obj=child()
# print(Obj)

"pratice question no 15"
# class parents:
#     def Hello_son(self):
#         print("Hello son")
# class Child(parents):
#     def __init__(self):
#         super().__init__()
#     def Yoo_dad(self):
#         print("Yoo dad")        
# obj=Child()
# obj.Hello_son()
# obj.Yoo_dad()

"pratice question no 16"
# class parents:
#     def show(self):
#         print("This is parents method")
# class Child(parents):
   
#     def show(self):
#         print("This is a child method")
#         super().show()
# obj=Child()
# obj.show()

"pratice question no 1*7=7"
# class Father:
#     def good_communication(self):
#         print("father have good communication skills")
# class Mother :
#     def good_cooking_skills(self):
#         print("Mother have good cooking skills ")
# class child(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("Children have both skills he can also make food and good communication skills")
# obj=child()
# obj.good_communication()
# obj.good_cooking_skills()
# print(obj)





    




        
        
        
        

        
        










        
        






        


        
    
        


        
        