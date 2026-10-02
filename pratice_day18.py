"Pratice question 1"
"Constructor +Method,person class banaao ,attributes:name,age,method:greet()-Hello my name is"

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print("Hello my name is",self.name)
#         print("MY age is ",self.age)
# p1=person("Harsh",20)
# p1.greet()

"Pratice question 2"
# class Mobile:
#     brand = "iPhone"   # class variable

#     def __init__(self, model, price):
#         self.model = model      # instance variable
#         self.price = price      # instance variable

#     def show(self):
#         print(self.model, "-", self.price, "-", Mobile.brand)


# # 2 objects
# m1 = Mobile("iPhone 15", 100000)
# m2 = Mobile("iPhone 16", 200000)

# # print details
# m1.show()
# m2.show()

# # comparison
# if m2.price > m1.price:
#     print("iPhone 16 is expensive compared to iPhone 15")
# else:
#     print("iPhone 15 is expensive compared to iPhone 16")


"Single Inheritance,Vehicle class,Method:start(),Bike class inherit kare aur start() call kare"
# class Vehicle():
#     def __init__(self,name):
#         self.name=name
#     def start(self):
#         print(self.name,"start successfully")
# class Bike(Vehicle):
#     pass
# b1=Bike("TVS")
# b1.start()
'''Method Overloading,1) Calculator class,2) Calculator class:,3)method add() jo ,2 numbers ka sum ,3 numbers ka sum kare
'''
# class calculator():
#     def add(self,*num):
#         total=0
#         for nums in num:
#             total+=nums
#         return total
# c=calculator()
# print(c.add(2,3))
# print(c.add(1,2,3))

"Method Overriding,1) company class,2)method works_hours-8,ITCompany class,4)Overide karke 10 hours return kare"
# class Company():
#     def Working_Hour(self):
#         return "Working Hours :8hours"
# class ITcompany(Company):
#     def working_hours(self):
#         return "Working Hours :10 hours"
# c=Company()
# it=ITcompany()
# print(c.Working_Hour())
# print(it.working_hours())
"Encapsulation 1) ATM class,2)private variable __pin,3)method:Check __pin()"
# class ATM:
#     def __init__(self,acount_no,pin):
#         self.acount_no=acount_no
#         self.__pin=pin
#     def get_pin(self):
#         return self.__pin
# A1=ATM(12345,1212)
# print(A1.get_pin())

"Polymorphism 1)Animal class:,2)Method:sound(),3)Dog,Cat class bana ke loop me sound () call karo"
# class Animals():
#     def sound(self):
#         print("Animals make sound")
# class Dog(Animals):
#     def sound(self):
#         print("Bhow,Bhow")
# class Cat(Animals):
#     def sound(self):
#         print("Meow,meow")
# animals=[Animals(),Dog(),Cat()]
# for i in animals:
#     i.sound()

"Multiple Inheritance 1) Teacher class-teach(),2)Researcher class - research() 3)professor class dono inherit kare"

# class Teacher:
#     def teach(self):
#         print("Teacher teaches the class")

# class Researcher:
#     def research(self):
#         print("Researcher finds new inventions")

# class Professor(Teacher, Researcher):
#     def work(self):
#         print("Professor teaches and does research")

# # object
# p = Professor()

# p.teach()      # Teacher class method
# p.research()   # Researcher class method
# p.work()       # Professor class method

"Magic Method(__Str__),1)Book class 2)attributes:title,price 3) object print karne par readable output aaye"
# class Book:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#     def __str__(self):
#         return f"Book Title:{self.title},price:${self.price}"
    
#     #Object
# b1=Book("Python Basics",299)
# b2=Book("Data Structure",499)
# print(b1)
# print(b2)
    
"Mini project -Shopping Cart"
# class ShoppingCart:
#     def __init__(self):
#         self.items={}
#     def add_item(self,item,price):
#         self.items[item]=price
#         print(item,"added to cart")
#     def remove_item(self,item):
#         if item in self.items:
#             del self.items[item]
#             print(item,"removed from cart")
#         else:
#             print("Item not found")
#     def total_price(self):
#         total=sum(self.items.values())
#         print("Total Price:$",total)

# cart=ShoppingCart()
# cart.add_item("Laptop",50000)
# cart.add_item("Mouse",500)
# cart.add_item("Keyboard",700)

# cart.total_price()
# cart.remove_item("Mouse")
# cart.total_price()




        
    





        








        








        