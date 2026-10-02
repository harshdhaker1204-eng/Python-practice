"pratice question no 1"
# class Animal:
#     def sound(self):
#         print("Animal make sound")
# class dog(Animal):
#     def sound(self):
#         print("Dogs are bark")
# D=dog()
# D.sound()
# D.sound()

"pratice question no 2"
# class Person:
#     def __init__(self):
#         print("Hello i am dad")
# class student(Person):
#     def __init__(self,Name,Roll_no):
#         super().__init__()
#         self.Name=Name
#         self.Roll_no=Roll_no
#     def displaY(self):
#         print("Student name is ",self.Name)
#         print("Student roll no is",self.Roll_no)
# S=student("Kanishk Rawal","0808IO231034")
# S.displaY()
        
"pratice question no 3"
# class vehicle:
#     def start_engine(self):
#         print("Vehicel engine start")
# class Bike(vehicle):
#     pass

# B1=Bike()

# B1.start_engine()

"pratice question no 4"
# class Employee:
#     def __init__(self,name,department):
#         self.name=name
#         self.department=department
#     def Employee_Details(self):
#         print("Employee name is ",self.name)
#         print("Department name is",self.department)

# class Manager:
#     def manager_details(self):
#         pass
# E=Employee("Sunil","IT")
# E.Employee_Details()

"pratice question no 5"
# class Mobile:
#     def __init__(self):
#         pass
# class SmartPhone(Mobile):
#     def __init__(self):
#         super().__init__()
#     print("New feature is megapixel camera")
# obj=SmartPhone()
# print(obj)


"pratice question no 6"

# class Animal:
#     def __init__(self,name):
#         self.name=name
        
# class Cat(Animal):
#     def __init__(self, name,color):
#         super().__init__(name)
#         self.color=color
#     def CN(self):
#         print("Animal name",self.name)
#         print("Cat color ",self.color)
# C=Cat("Shiro","White")
# C.CN()

"pratice question no 7"
# class Father :
#     def __init__(self):
#         print("Hello i Am father ")
# class son(Father):
#     def __init__(self):
#         super().__init__()
#         print("Hii i am son")
# S=son()
# S.__init__()
# print(S)

"pratice question no 8"
# class College:
#     def __init__(self,name):
#         self.name=name
# class Department(College):
#     def __init__(self, name,D_name):
#         super().__init__(name)
#         self.D_name=D_name
#     def N1(self):
#         print("College name ",self.name)
#         print("Department name is",self.D_name)
# D=Department("IPS","CSE")
# D.N1()

        
"pratice question no 9"

# class Book:
#     def __init__(self, B_name):
#         self.B_name = B_name


# class Author(Book):
#     def __init__(self, B_name, A_name):
#         super().__init__(B_name)
#         self.A_name = A_name

#     def N1(self):
#         print("Book name:", self.B_name)
#         print("Author name is:", self.A_name)


# A = Author("Harsh", "how are you")

# A.N1()

"pratice question no 10"
# class Shape:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#     def area_of_R(self):
#         print("Area of rectangle is",self.length*self.width)
# R=Rectangle(5,10)
# R.area_of_R()
"pratice question no 11"
# class Bird:
#     def fly(self):
#         print("Bird can fly")
# class Penguim(Bird):
#     def __init__(self):
#         super().__init__()
#     def fly(self):
#         print("Penguin can not fly")
# P=Penguim()
# P.fly()

"pratice question no 12"
# class Bank:
#     def __init__(self,name):
#         self.name=name
# class SBI(Bank):
#     def __init__(self, name,P,T,R):
#         self.P=P
#         self.T=T
#         self.R=R
#         super().__init__(name)
#     def Interest_rate(self):
#         print("Name",self.name)
#         print("Total Interest is",(self.P*self.T*self.R)/100,"rupees")
# S=SBI("ABC",1000,1,2.5)
# S.Interest_rate()

"pratice question no 13"
# class Vehicle:
#     def info(self):
#         print("Hello this is Vehicle")
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#     def info(self):
#         print("This is car")
# C=Car()
# C.info()
# V=Vehicle()
# V.info()

"pratice question no 14"
# class Person:
#     def Profession(self):
#         print("This is just normal person")
# class Teacher:
#     def Profession(self):
#         print("This person is Teacher ")
# P=Person()
# T=Teacher()
# P.Profession()
# T.Profession()

"pratice question no 15"
# class shape:
#     def __init__(self,radius):
#         self.radius=radius
# class Circle(shape):
#     def __init__(self, radius):
#         super().__init__(radius)
#     def area_of_Circle(self):
#         print("area of circle",3.14*self.radius*self.radius)
# C=Circle(10)
# C.area_of_Circle()

"pratice question no 16"
# class A:
#     def __init__(self):
#         print("Hello A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Hello B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Hello C")

# C1=C()
# print(C1)

"pratice question no 17"
# class GrandParents:
#     def __init__(self,House):
#         self.House=House
#         print("Grandparents have ",self.House)
# class Parents(GrandParents):
#     def __init__(self, House,Car):
#         super().__init__(House)
#         self.Car=Car
#         print("Parents Have",self.Car)
# class Child(Parents):
#     def __init__(self, House, Car,Bike):
#         super().__init__(House, Car)
#         self.Bike=Bike
#         print("Child have",self.Bike)
# C=Child("Villa","BMW","KTM")
# print(C)

"pratice question no 18"
# class Vehicle:
#     def __init__(self):
#         print("Its vehicle")
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print("Its just car")
# class Electric_Car(Car):
#     def __init__(self):
#         super().__init__()
#     def Battery(Self):
#         print("Good battery capacity")
#     def Charge_method(Self):
#         print("Electric")
# E=Electric_Car()
# print(E)
# E.Battery()
# E.Charge_method()

"pratice question no 19"
# class Animal:
#     def __init__(self):
#         print("Animal make sound")
# class Cat(Animal):
#     def Cat_sound(self):
#         print("Meow,Meow")
# class Dog(Animal):
#     def dog_sound(self):
#         print("Bark Bark")
# D=Dog()
# D.dog_sound()
# C=Cat()
# C.Cat_sound()
# A=Animal()
# print(A)

# "pratice question no 20"
# class Shape:
#     def __init__(self,length,width,Base,Height):
#         self.length=length
#         self.width=width
#         self.Base=Base
#         self.Height=Height
# class Rectangle(Shape):
#     def __init__(self, length, width,Base,Height):
#         super().__init__(length, width,Base,Height)
#     def area_of_R(self):
#         print("Area of Rectangle",self.length*self.width)
# class Triangle(Shape):
#     def __init__(self,length,width,  Base, Height):
#         super().__init__( length,width,Base, Height)
#     def Area_of_T(Self):
#         print("Area of Triangle is",(Self.Base*Self.Height)/2)
# Re=Rectangle(10,4,1,1)
# Re.area_of_R()

# Tri=Triangle(10,4,1,1)
# Tri.Area_of_T()






        
        





        



        


        



        





        




