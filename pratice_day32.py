"Question no 1 Division Error"
# try:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter Second number:"))
#     result=a/b
#     print("result",result)
# except ZeroDivisionError:
#     print("Error because 0 can not divide")
"Question no 2 valueError"
# try:
#     num=int(input("Enter a value="))
#     print("value is",num)
# except ValueError:
#     print("Please Enter Integer number")

"Question no 3 indexError"

# nums=[10,20,30,40]
# try:
#     index=int(input("Enter a index"))
#     print("value",nums[index])
# except IndexError:
#     print("The index is out of range please enter in range index")

"Question no 4 file not found error"
# try:
#     file=open("data.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found in data bases")

"Question no 5 Multiple Except Blocks"
# nums=[10,20,30]
# try:
#     value=int(input("Enter value"))
#     index=int(input("Enter index"))

#     print(value/nums[index])
# except ValueError:
#     print("please enter integer type value")
# except IndexError:
#     print("The index is out of range please enter right index value")
# except ZeroDivisionError:
#     print("please enter a positive number")


"Question no 6 try-except-finally"

# try:
#     a=int(input("Enter first number"))
#     b=int(input("Enter second number"))
#     result=a/b
#     print("result",result)
# except Exception as e:
#     print("Error",e)
# finally:
#     print("Program finished")

"question no 7 dictionary key value error"

# student={"name":"priyans","marks":92}
# try:
#     key=input("Enter  key:")
#     print("value:",student[key])
# except KeyError:
#     print("invalid key please enter valid key")

"Question no 8 type error"
# try:
#     a=input("Enter first number")
#     b=input("Enter second number")

#     print(int(a)+int(b))
# except TypeError:
#    print("error:mismatch")
# except ValueError:
#     print("Type error")


"question no 9 Custom valuesError"
# try:
#     age=int(input("Enter age:"))
#     if age<0:
#         raise ValueError("Age negative can not be negative")
#     print("age",age)
# except ValueError as e:
#     print("Error:",e)

"question 10 try and except inside the loops"
# Values=[10,10,5,10,20]
# for v in Values:
#    try:
#      print(100/v)
#    except ZeroDivisionError:
#      print("number must be greater than 0")







