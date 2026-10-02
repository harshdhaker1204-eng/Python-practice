"Pratice question no 1"
# num=int(input("Enter a number"))
# if (num>0):
#     print("Number is positive")
# elif(num==0):
#     print("Number is zero")
# else:
#     print("Number is negative")
"Pratice question no 2"
# num=int(input("Enter a number"))
# if (num%2==0):
#     print("Even number")
# else:
#     print("Odd number")

"pratice question no 3"

# num1=int(input("Enter a num1"))
# num2=int(input("Enter a num2"))
# if (num1>num2):
#     print(f"{num1}is greater then {num2} ")
# elif(num1==num2):
#     print(f"{num1} and {num2} both are equal")
# else:
#     print(f"{num2} is greater then {num1}")

"Pratice question no 4"
# num1=int(input("Enter a num1"))
# num2=int(input("Enter a num2"))
# num3=int(input("Enter a num3"))



# if (num1>num2 and num1>num3 ):
#     print(f"num1 {num1} is greater then num2 {num2} ,num3 {num3}")
# elif (num2>num1 and num1>num1 ):
#     print(f"num2 {num2} is greater then num2 {num1} ,num1 {num3}")
# elif (num3>num2 and num3>num1 ):
#     print(f"num1 {num1} is greater then num2 {num2} ,num3 {num3}")   
# else:
#     print("all three number are equal")

"Pratice question no 5"
# num1=int(input("Enter a num1"))
# if(num1%5==0):
#     print("Number is divisible by 5")
# else:
#     print("Number is not divisible by 5")

"Pratice question no 6"
# num1=int(input("Enter a num1"))
# if ((num1<=20) and (num1>=10)):
#     print("Number in between 10 and 20")
# else:
#     print("Number is not in between 10 to 20")

"Pratice question no 7"
# ch=input("Enter a character")
# if ch in ('a','e','i','o','u','A','E','I','O','U'):
#     print("It is a vowel")
# else:
#     print("It is a consonant")

"Pratice question no 8"
# year=int(input("Enter a year"))
# if (year%4==0 and  year%100!=0 ) or (year%400==0):
#     print("Leap year")
# else:
#     print("Not a leap year")

"Pratice question no 9"
# num1=int(input("Enter a num1"))

# if ((num1%7==0) and (num1%3==0)):
#     print("Number is divisible by 7 and 3")
# else:
#     print("Number is not divisible by 3 and 7")

"Pratice question no 10"
# age=int(input("Enter a age"))
# if (age>=18):
#     print("Age is eligible for vote ")
# else:
#     print("Age is not eligible for vote")

"Pratice question no 11"
# num=int(input("Enter a number"))
# if ((num>=100) and (num<=999)):
#     print("Number is three digit no")
# else:
#     print("Number is not a three digit no")

"Pratice question no 12"
# num1=int(input("Enter a num1"))
# num2=int(input("Enter a num2"))
# num3=int(input("Enter a num3"))

# if((num1<num2) and (num1<num2)):
#     print(f"{num1} is less then {num2} and {num3}")
# elif((num2<num1) and (num2<num3)):
#     print(f"{num2} is less then {num1} and {num3}")
# else:
#     print(f"{num3} is less then {num1} and {num2}")

"Pratice question no 13"
# num=(input("Enter a number"))

# if num==num[::-1]:
#     print("Its palindrome")
# else:
#     print("its not a palindrome")
"Pratice question no 14"

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
"Pratice question no 15"
# char=input("Enter a character")
# if char.lower():
#     print("Its a lowercase")
# elif char.isupper():
#     print("Its a uppercase")
# else:
#     print("not a alphabet")

"Pratice question no 16"

# num=int(input("Enter a num"))
# sqrt=num**0.5
# if sqrt==int(sqrt):
#     print("Perfect square")
# else:
#     print("Nota perfect square")

"Pratice question no 17"
# num=int(input("Enter a num"))
# if (num>100):
#     print(f"number{num }is greater then 100 ")
# else:
#     print("Good night")

"Pratice question no 18"
# marks_grade=int(input("Enter your marks"))

# if marks_grade>=90 and marks_grade<=100:
#     print("You got the A grade")
# elif marks_grade>=75 and marks_grade<=89:
#      print("You got the B grade")
# elif marks_grade>=50 and marks_grade<=74:
#      print("You got the c grade")
# else:
#      print("Fail")

"Pratice question no 19"
# units=int(input("Enter your units"))

# if units<=100:
#     units*=5
#     print(f"Your Electricity bill {units} rupees")
# elif ((units>100) and (units<200)):
#     units*=7
#     print(f"Your Electricity bill {units} rupees")
# elif(units>200):
#     units*=10
#     print(f"Your Electricity bill {units} rupees")
# else:
#     print("-----")
"Pratice question no 20"
# a=int(input("Enter a a"))
# b=int(input("Enter a b"))
# c=int(input("Enter a c"))

# if a+b+c==180 and a>0 and b>0 and c>0:
#     print("valid triangle")
# else:
#     print("invalid triangle ")

"Pratice question no 21"

# a=int(input("Enter  a"))
# b=int(input("Enter  b"))
# c=int(input("Enter  c"))

# if a==b==c:
#     print("Its a equilateral triangle")

# elif ((a==b) or (b==c) or (a==c)):
#     print("isoscales")
# else:
#     print("scalene")


"Pratice question no 22"
# num=int(input("Enter a armstrong number"))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==num:
#     print("Its armstrong")
# else:
#     print("Its not armstrong")

"pratice question 23"
# num=int(input("Enter a number"))
# if num%11==0:
#     print("Its divisible by 11")
# else:
#     print("Its not divisible by 11")
"pratice question 24"

# month = int(input("Enter a month number: "))

# months = {
#     1:"January",
#     2:"February",
#     3:"March",
#     4:"April",
#     5:"May",
#     6:"June",
#     7:"July",
#     8:"August",
#     9:"September",
#     10:"October",
#     11:"November",
#     12:"December"
# }

# if month in months:
#     print(months[month])
# else:
#     print("Invalid month")

"pratice question 25"
# temp=int(input("Enter a temperature"))

# if temp>40:
#     print("Very hot")
# elif temp>=25 and temp<=40:
#     print("Warm temperature")
# elif temp>=10 and temp<=24:
#     print("cool temperature")
# else:
#     print("very cool")


"pratice question 25"

# salary = int(input("Enter your salary: "))

# if salary < 250000:
#     print("No tax")

# elif salary >= 250000 and salary < 500000:
#     tax = salary * 0.05
#     print("Tax =", tax)

# elif salary >= 500000 and salary < 1000000:
#     tax = salary * 0.20
#     print("Tax =", tax)

# elif salary >= 1000000:
#     tax = salary * 0.30
#     print("Tax =", tax)

# else:
#     print("Invalid input")

"pratice question 27"

# H=int(input(" H"))
# P=int(input("P"))
# B=int(input("B"))


# if H**2==P**2 + B**2:
#     print("Its pythagoras")
# else:
#     print("Its not a pythagoras")

"pratice question 28"

# H=int(input(" H"))
# sum=0
# for i in range(1,H):
#     if H%i==0:
#         sum=sum+i
# if sum==H:
#     print("Perfect Square")
# else:
#     print("Not a perfect square")

"pratice question 29"
# hour = int(input("Enter hour (0-23): "))

# if hour >= 5 and hour < 12:
#     print("Morning")

# elif hour >= 12 and hour < 17:
#     print("Afternoon")

# elif hour >= 17 and hour < 21:
#     print("Evening")

# elif hour >= 21 or hour < 5:
#     print("Night")

# else:
#     print("Invalid Time")

"pratice question 30"
year = int(input("Enter a year: "))

if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")





    







 






    
    


    










    


     


