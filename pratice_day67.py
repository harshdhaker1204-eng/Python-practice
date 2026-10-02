"Pratice question no 1"
# def Function_start(Func):
#     def my_inner():
#         return Func().upper()
#     return my_inner

# @Function_start
# def My_Function():
#     return "Function started"
# print(My_Function())

"Pratice question no 2"
# import time
# #Decorator function
# def execution_time(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time() #start timer
#         result=func(*args,**kwargs)
#         end_time=time.time() #End timer

#         print(f"Execution time :{end_time-start_time:.6f} second")
#         return result
#     return wrapper
# #using the decorator

# @execution_time
# def sample_function():
#     for i in range(1000000):
#         pass
#     print("Function executed")
# sample_function()

"Pratice question no 3"
# def Uppercase_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# @Uppercase_decorator
# def greet():
#     return "hello sir"
# print(greet())

"Pratice question no 4"
# def login_required(func):
#     def wrapped(is_login,*args,**kwargs):
#         if is_login:
#             return func(*args,**kwargs)
#         else:
#             return "access denied! please login first"
#     return wrapped
# @login_required
# def view_profile():
#     return "welcome to your profile"
# print(view_profile(False))
# print(view_profile(True))

"Pratice question no 5"
# def run_function(func):
#     def wrapped(times):
#        for i in range(times):
#            print(func())
#     return wrapped
# @run_function
# def call_function():
#     return "Hello fuction call 3 times automatically"
# call_function(3)
    
"Pratice question no 6"
# def Argument_logger(func):
#     def wrapper(*args,**kwargs):
#         print("Positional Arguments",args)
#         print("Keyword Arguments",kwargs)
#         return func(*args,**kwargs)
#     return wrapper

# @Argument_logger
# def student_detail(name,age,course="Python"):
#     print(f"Student name:{name}")
#     print(f"student age:{age}")
#     print(f"Student Course:{course}")
# student_detail("Vedant jain",20,course="Data science")

"Pratice question no 7"
# def safe_division(func):
#     def wrapper(a,b):
#         if b==0:
#             return "Error:Division by zero is not allowed"
#         return func(a,b)
#     return wrapper
# #using the decorator
# @safe_division
# def divide(a,b):
#     return a/b
# #Function calls
# print(divide(10,2))
# print(divide(10,0))

"Pratice question no 8"
# def call_counter(func):
#     count=0
#     def wrapper(*args,**kwargs):
#         nonlocal count
#         count+=1
#         print(f"Function called {count} times")
#         return func(*args,**kwargs)
#     return wrapper
# #using the decorator
# @call_counter
# def greet():
#     print("Hello!")
# greet()
# greet()
# greet()
# greet()

"Pratice question no 9"
# def admin_only(func):
#     def wrapper(user_role,*args,**kwargs):
#         if user_role=="admin":
#            return func(*args,**kwargs)
#         else:
#             return "Access Denied ! Admins only"
#     return wrapper

# #using the decorator
# @admin_only
# def delete_data():
#     return "Data deleted successfully"

# #function calls
# print(delete_data("admin"))
# print(delete_data("user"))

"Pratice question no 10"
#First decorator
# def before_decorator(func):
#     def wrapper():
#         print("Before")
#         return func()
#     return wrapper
# #Second decorator
# def after_decorator(func):
#     def wrapper():
#         result=func()
#         print("After")
#         return result
#     return  wrapper
# #Applying both decorators
# @after_decorator
# @before_decorator
# def greet():
#     return "Hello"
# greet()





 
















