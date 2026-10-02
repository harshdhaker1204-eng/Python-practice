"Write a program to check if a number is positive, negative or zero"

# number=15

# if number>0:
#     print("Number is positive")
# elif number<0:
#     print("Number is negative")
# else:
#     print("Number is zero")

"Input a number and check if it is even or odd"

# Number=int(input("Enter a Even or odd number:"))

# if Number%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

"Take two numbers and print which one is greater "

# Number1= 100
# Number2=200

# if Number1>Number2:print("Number1 is greater than Number2",Number1)
# else:
#     print("Number2 is greater than Number1:",Number2)

"Input three numbers and print the largest amoung them"

# a=int(input("Enter Number a="))
# b=int(input("Enter Number b="))
# c=int(input("Enter Number c="))

# if a>b and a>c:
#     print("a is greater than b and c=",a)
# elif b>a and b>c:
#     print("b is greater than a and c=",b)
# elif c>a and c>b:
#     print("c is greater than a and b= ",c)
# else:
#     print("All the three values are equal")


"Check whether a year is  a leap year or not"
# year=int(input("Enter a year"))

# if year%400==0:
#     print("leap year")

# elif year%100==0:
#     print("Not a leap year")

# elif year%4==0:
#     print("Leap year")

# else:
#     print("Not a leap year")

"Take a users age and check if they are eligible to vote(18+ or not)."

# user_age=int(input("Enter your age"))

# if user_age >= 18:
#     print("You are eligible for the vote:")
# else:
#     print("You are not eligible for the vote:")

"input a password and check if it is  correct(compare with a stored password)"

# correct_password="python123"

# user_password=input("Enter your password:")

# if user_password == correct_password:
#     print("Access Granted")
# else:
#     print("Incorrect password")

"input marks and print the grade(A/B/C/D/Fail)."
# Marks=int(input("Enter your marks:"))

# if Marks>=90:
#     print("Grade A")
# elif Marks>=89:
#     print("Grade B")
# elif Marks >79:
#     print("Grafe C")
# elif Marks>60:
#     print("Grade D")
# else:
#     print("Fail")

"Check if a number is divisible by 5 and 11 or not"

# number = int(input("Enter a number: "))

# if number % 5 == 0 and number % 11 == 0:
#     print("Number is divisible by 5 and 11")

# elif number % 5 == 0 and number % 11 != 0:
#     print("Number is only divisible by 5")

# elif number % 5 != 0 and number % 11 == 0:
#     print("Number is only divisible by 11")

# else:
#     print("Number is not divisible by 5 and 11")

"Check if a character is vowel or consonant."

# character=input("Enter vowel or consonant")

# if character in "aieouAIEOU":
#     print("Character is vowel")
# else:
#     print("Character is consonant")

"input a number ann check if it is prime or not"

# num=int(input("Enter a number"))

# if num<=1:
#     print("Not a prime number")

# elif num == 2 or num ==3:
#     print("Prime number")

# elif num % 2==0:
#     print("Not a prime number")

# elif num %3==0:
#     print("Not a prime number")

# else:
#     print("Prime number")

"Input temperature and display"

# temperture=int(input("Enter a temperture"))

# if temperture<=15:
#     print("Cold")
# elif temperture>15 :
#     print("Warm")
# else:
#     print("Hot")

"Input a number and display whether it is single-digit,duoble-digit or more"
# num=int(input("Enter a number"))

# if num>=-9 and num<=9:
#     print("Single digit")

# elif num>=-99 and num<99:
#     print("double digit")

# else:
#     print("More then two digits")

"Input a number and check if it is perfect square or not"
# num=int(input("Enter a number"))
# root=int(num**0.5)

# if root*root == num:
#     print("Perfect square")
# else:
#     print("Not a perfect square")

"Shop discount program (Python code)"
# amount=float(input("Enter your amount:"))

# if amount>5000:
#     discount=amount*0.10
#     final_price=amount-discount
#     print("discount applied",discount)
#     print("Final amount to pay",final_price)

# else:
#     print("No discount applied")
#     print("Final amount to pay",amount)

"Take a username and check"
" if it contains less than 6 characters-invalid"
"else valid"

# username=input("Enter your username")

# if len(username)<6:
#     print("Invalid user name ")
# else:
#     print("Valid username")

"Check if a number is within the range 1 to 100 or not"

# num=int(input("Enter a number"))

# if num>=1 and num<=100:
#     print("Number in range")

# else:
#     print("Number is not in range")

"Input 3 sides and check if they form a valid triangle"
# a=int(input("Enter a side a"))
# b=int(input("Enter a side b"))
# c=int(input("Enter a side c"))

# if a+b>c and a+c>b and b+c>a:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

"Traffic light simulation"
"input: red , Yellow, green"
"Output appropiate action(stop/wait/go)"

# light=input("Enter a traffic light(red),(green),(yellow)=").lower()

# if light=="red":
#     print("stop")
# elif light =="yellow":
#     print("wait")
# elif light =="green":
#     print("go")
# else:
#     print("Invalid traffic light")






