import re
"pratice question 1"
"Lowercase letters [a-z]"
# pattern=r'^[a-z]+$'
# print(bool(re.match(pattern,"hello"))) #True
# print(bool(re.match(pattern,"Hello123"))) #False

"pratice question 2"
"only digits(0-9)"
# pattern=r'^[0-9]+$'
# print(bool(re.match(pattern,"12345"))) #True
# print(bool(re.match(pattern,"hello123"))) #False

"pratice question 3"
"Email Id"
# pattern=r'[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
# print(bool(re.match(pattern,"test@gmail.com")))
# print(bool(re.match(pattern,"user_1@yahoo.in")))

"pratice question 4"
"Indian Mobile Number"
# pattern=r'^[6-9][0-9]{9}$'
# print(bool(re.match(pattern,"9876543210")))
# print(bool(re.match(pattern,"1234567890")))

"pratice question 5"
"Alphabates +space only"

# pattern=r'^[A-Za-Z]+$'
# print(bool(re.match(pattern,"Rahul Sharma"))) #True
# print(bool(re.match(pattern,"Rahul123"))) #False

"pratice question 6"
"password(8 chars,upper,lower,digit)"
# pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
# print(bool(re.match(pattern,"Abc12345"))) #True
# print(bool(re.match(re.match(pattern,"abc123"))))

"pratice question 7"
"Date (DD/MM/YYYY)"
# pattern=r'^\d{2}/\d{2}/\d{4}$'
# print(bool(re.match(pattern,"05/02/2026")))

"pratice question 8"
"URL (http / https)"
# pattern=r'https?:\/\/[a-zA-Z0-9.-]+\[a-zA-Z]{2,}$'
# print(bool(re.match(pattern,"https://google.com")))
# print(bool(re.match(pattern,"https://example.in")))

"pratice question 9"
# pattern=r'^.+\.com$'
# print(bool(re.match(pattern,"amazon.com")))
# print(bool(re.match(pattern,"amazon.in")))


"pratice question 10"
# pattern =r'^[A-Za-z]{3,4}$'
# print(bool(re.match(pattern,"cat")))
# print(bool(re.match(pattern,"door")))
# print(bool(re.match(pattern,"house")))



