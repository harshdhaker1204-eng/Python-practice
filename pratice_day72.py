import re
"Pratice question no 1"
# txt="Hello my name is harsh"
# x=re.findall(r"\AHello+",txt)
# print(x)
# if x:
#     print("Hello is found")
# else:
#     print("Hello is not found")

"Pratice question no 2"
# txt="Hello i am Python"
# x=re.findall(r"\A\w+",txt)
# print(x)

"Pratice question no 3"
# txt="cat is a animal cat is is is is is is is is is is is"
# x=re.findall(r"cat\b",txt)

# print(x)
# if x:
#     print("word is present ")
# else:
#     print("word is not present")


"Pratice question no 4"
# txt="cat is a animal cat is is is is is is is is is is is"
# x=re.findall(r"is\b",txt)
# print(x)
# count=0
# for _ in x:
#     count+=1
# print("There  are" ,count,"is appear in the txt")

"Pratice question no 5"
# txt="catdogcatdog"
# # x=re.findall(r"cat\B",txt)
# x=re.findall(r"\Bcat",txt)
# print(x)

"Pratice question no 6"
# txt="I am coding and sing,dancing,playing"
# x=re.findall(r"\b\w+ing\b",txt)
# print(x)

"Pratice question no 7"
# txt="0hello 1My 2name 3is 4james 5bobby 77fisher"
# x=re.findall(r"\d+",txt)
# print(x)

"Pratice question no 8"
# txt="call on 7982538112 or 9340056413"
# x=re.findall(r"\d+",txt)
# print(x)

"Pratice question no 9"
# txt="0hello 1My 2name 3is 4james 5bobby 77fisher"
# x=re.findall(r"\D+",txt)
# print(x)

"Pratice question no 10"
# password="Harsh123@45"
# x=re.findall(r"\D",password)
# print(x)
# print("Count",len(x))

"Pratice question no 11"
# txt="Python is easy\tto learn"
# x=re.findall(r"\s",txt)
# print(x)
# print("Count",len(x))

"Pratice question no 12"
# txt="Python is easy\tto learn"
# x=re.split(r"\s",txt)
# print(x)

"Pratice question no 13"
# txt="Python is easy\tto learn"
# x=re.findall(r"\S+",txt)
# print(x)
# print(len(x))

"Pratice question no 14"

# txt="Python is\tawesome"
# x=re.findall(r"\S+",txt)
# print(x)

"Pratice question no 15"
# user_name="Optimus_prime@12345"
# x=re.findall(r"\w+",user_name)
# x=re.findall(r"\w",user_name)
# print(x)

"Pratice question no 16"
# txt="name=alok\nage=20\nsex=male"
# x=re.findall(r"\w+",txt)
# print(x)

"Pratice question no 17"
# user_name="Optimus_prime@12345 ####$$$@@"
# x=re.findall(r"\W+",user_name)

# # x=re.sub(r"\W+"," ",user_name)
# print(x)

"Pratice question no 18"
# txt="Hello! Python How are you? Python@2025"
# x=re.findall(r"\W",txt)
# print(x)

"Pratice question no 19"
# txt="Hello_kids.py"
# x=re.findall(r".py\Z",txt)
# print(x)
# if x:
#     print("End with .py")
# else:
#     print("Not end with .py")

"Pratice question no 20"

# txt="This is the END"
# x=re.findall(r"END\Z",txt)
# print(x)
# if x:
#     print("True")
# else:
#     print("False")






























