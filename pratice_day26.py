"Email ID Validate karna"
import re
# email="test123@gmail.com"
# pattern=r'^[\w\,-]+@\w\.-]+\.\w+$'

# if re.match(pattern,email):
#     print("Valid Email")
# else:
#     print("Invalid Email")

"Check the 10 digit mobile number"
# mobile="9876543210"
# pattern=r'^[6-9]\d{9}$'
# print(bool(re.match(pattern,mobile)))
"check string "
# text ="12345"
# pattern=r'\d+$'
# print(bool(re.match(pattern,text)))

"Check alphabets in string"
# text="Harsh"
# pattern=r'^[A-Za-Z]+$'
# print(bool(re.match(pattern,text)))
"Check password strong or not"
# 
# password="Harsh@123"
# pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=*\d)(?=.8[@$!%*?&]).{8,}$'
# print(bool(re.match(pattern,password)))

"get  all number in sentence"
# text="my age is 21 and roll no is 45"
# number=re.findall(r'\d+',text)
# print(number)

"get all the words form the sentence"
# text="Python is very easy"
# words=re.findall(r'\w+',text)
# print(words)
"remove the extra spaces"

# text="Python is easy"
# result=re.sub(r'\s+','',text)
# print(result)
"Check the date format"
# date="25-01-2026"
# pattern=r'^\d{2}-\d{2}-|d{4}$'
# print(bool(re.match(pattern,date)))
"replace any word"
# text="I love java"
# result=re.sub(r'Java','Python',text)
# print(result)

"Email validation"


# email = "HarshDhaker1204@gmail.com"

# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")
"Check the 10 digit mobile number"
# mobile="9876543210"
# pattern=r'^[6-9]\d{9}$'
# print(bool(re.match(pattern,mobile)))
"password strength check"
# password = "Abc@1234"
# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).{6,}$'
# print(bool(re.match(pattern, password)))

"Extract all numbers from string"
# text="My age is 22 and my brother is 25"
# numbers=re.findall(r'\d+',text)
# print(numbers)
"Check only alphabets"
# text="Python"
# print(bool(re.match(r'^[A-Za-z]+$',text)))
"Replace spaces with underscore"
# text="Hello world python"
# result=re.sub(r'\s+','_',text)
# print(result)
"find all words starting with 'P"
# text = "Python Programming Pratice"
# words = re.findall(r'\bP\w+', text)
# print(words)

"check date format"
# date="25-01-2026"
# pattern=r'\d{2}-\d{2}-\d{4}$'
# print(bool(re.match(pattern,date)))

"Remove speciak characters"
# text="Hello@# world!"
# clean=re.sub(r'[^A-Za-z0-9]','',text)
# print(clean)

"Count words in string"
# text="Python is very easy to learn"
# words=re.findall(r'\b\w+\b',text)
# print(len(words))





