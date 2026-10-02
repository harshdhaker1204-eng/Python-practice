"find the sum of array"
# arr1=[2,3,6]
# total=0
# for i in arr1:
#     total+=i
# print("the sum of array is",total)

"Find the maximum element of array"
# arr2=[10,25,5,40]
# print("The maximum element of array is",max(arr2))

"Find the minimum element of array"
# arr3=[8,3,15,1]
# print("The minimum element of array is",min(arr3))

"print reverse the array"
# arr4=[1,2,3,4]
# arr4.reverse()
# print(arr4)

"Even numbers count karo"

# arr=[1,2,4,7,8]
# even=0
# for i in arr:
#   if i%2==0:
#      even+=1
# if even==0:
#    print("There is no even numbers")
# else:
#    print("The total number even number are",even)

"Find the sum of Even and odd number"
# arr=[1,2,3,4,5,6,7,8,9,10]
# even=0
# odd=0
# for i in arr:
#     if i%2==0:
#         even+=i
#     elif i%2!=0:
#         odd+=i
#     else:
#         print("There is no number")
# print("The sum of even number are",even)
# print("The sum of odd number are",odd)

"Check element present or not"
# arr=[1,2,3,4,5,6]
# num=2
# if num in arr:
#     print("Element is present")
# else :
#     print("Element is not present")

"Find the duplicate element in arr"
# arr = [1, 2, 3, 2, 4, 5, 1, 6]

# duplicates = []

# for num in arr:
#     if arr.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate elements are:", duplicates)

"Find the second largest element of array"
# arr = [1,2,3,4,5,6,7,8,9,10]

# arr.sort()
# print("Second largest element is:", arr[-2])

"Question 1: Private Variable Access"

# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.__marks=marks

#     def get_marks(self):
#         return self.__marks
# S1=Student("Vedant",20)
# print("The student name is ",S1.name)
# print(S1.get_marks())

"Getter and setter"
# class BankAccount():
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance   # private variable

#     # Getter
#     def get_balance(self):
#         return self.__balance
    
#     # Setter
#     def set_balance(self, amount):
#         if amount > 0:
#             self.__balance = amount
#         else:
#             print("Balance must be positive")


# p1 = BankAccount("Tobias", 25000)

# print(p1.get_balance())      # getter

# p1.set_balance(200000)       # setter
# print(p1.get_balance())


"Read only data"

# class Employee():
#     def __init__(self,name,emp_id):
#         self.name=name
#         self.__emp_id=emp_id

#     def get_emp_id(self):
#         return self.__emp_id
    
#     def set_em_id(self):
#         if self.__emp_id>0:
#             self.__emp_id
#         else:
#             print("There is no id")

# E1=Employee("Vedant",20)
# print("The student name is ",E1.name)
# print(E1.get_emp_id())

"Encapsulation with validation"

# class Mobile:
#     def __init__(self, price):
#         self.__price = price     # private variable

#     def get_price(self):
#         return self.__price

#     def set_price(self, amount):
#         if amount > 1000:
#             self.__price = amount
#         else:
#             print("Invalid Price")
# M = Mobile(300)
# print(M.get_price())   # get old price

# M.set_price(1500)      # valid price
# print(M.get_price())

# M.set_price(500)       # invalid price


"Password Protection"
# class User:
#     def __init__(self, password):
#         self.__password = password   # private variable

#     def get_password(self):
#         return self.__password

#     def set_password(self, new_password):
#         if len(new_password) > 6:
#             self.__password = new_password
#         else:
#             print("Weak password")
# U = User("abc123")
# print(U.get_password())

# U.set_password("pass")        # weak
# U.set_password("strong123")   # strong

# print(U.get_password())


        


    

    
        
    


        

